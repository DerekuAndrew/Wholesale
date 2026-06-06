from datetime import datetime, timezone
from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status
from dtos.sale.sale_create import SaleCreateDTO
from dtos.sale.sale_update import SaleUpdateDTO
from models.sale import Sale
from models.sale_detail import SaleDetail
from repositories.product_repository import ProductRepository
from repositories.sale_repository import SaleRepository
from services.location_service import LocationService

class SaleService:
    @staticmethod
    def get_sales(db: Session):
        return SaleRepository.get_sales(db = db)

    @staticmethod
    def find_sale(sale_id: int, db: Session):
        sale = SaleRepository.find_sale(sale_id = sale_id, db = db)

        if not sale or sale.status == "DELETED":
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Sale not found"
            )

        return sale

    @staticmethod
    def create_sale(dto: SaleCreateDTO, db: Session):
        # Validamos la sucursal antes de armar la venta
        LocationService.find_location(location_id = dto.location_id, db = db)

        now = datetime.now(timezone.utc)
        details = SaleService.build_details(details = dto.details, db = db)
        total = sum(detail.subtotal for detail in details)
        sale = Sale(
            folio = "PENDING",
            location_id = dto.location_id,
            datetime = now,
            total = total,
            status = dto.status,
            created_at = now,
            updated_at = now,
            details = details
        )

        SaleService.discount_stock(details = details, db = db)
        return SaleRepository.create_sale(data = sale, db = db)

    @staticmethod
    def update_sale(dto: SaleUpdateDTO, db: Session):
        # Regresamos el stock anterior antes de reemplazar los detalles
        sale = SaleService.find_sale(sale_id = dto.id, db = db)
        LocationService.find_location(location_id = dto.location_id, db = db)
        SaleService.restore_stock(details = sale.details, db = db)

        try:
            details = SaleService.build_details(details = dto.details, db = db)
        except HTTPException:
            SaleService.discount_stock(details = sale.details, db = db)
            raise

        data = Sale(
            id = sale.id,
            location_id = dto.location_id,
            total = sum(detail.subtotal for detail in details),
            status = dto.status,
            updated_at = datetime.now(timezone.utc)
        )

        SaleService.discount_stock(details = details, db = db)
        updated_sale = SaleRepository.update_sale(data = data, details = details, db = db)

        if not updated_sale:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Sale not found"
            )

        return updated_sale

    @staticmethod
    def delete_sale(sale_id: int, db: Session):
        # Marcamos la venta como eliminada y regresamos el inventario
        sale = SaleService.find_sale(sale_id = sale_id, db = db)
        SaleService.restore_stock(details = sale.details, db = db)
        return SaleRepository.delete_sale(
            sale_id = sale_id,
            updated_at = datetime.now(timezone.utc),
            db = db
        )

    @staticmethod
    def build_details(details, db: Session):
        # Validamos el stock acumulado por producto
        sale_details = []
        requested_stock = {}

        for detail in details:
            product = ProductRepository.find_product(product_id = detail.product_id, db = db)

            if not product or not product.active:
                raise HTTPException(
                    status_code = status.HTTP_404_NOT_FOUND,
                    detail = "Product not found"
                )

            requested_stock[product.id] = requested_stock.get(product.id, 0) + detail.quantity

            if product.stock < requested_stock[product.id]:
                raise HTTPException(
                    status_code = status.HTTP_400_BAD_REQUEST,
                    detail = f"Insufficient stock for product {product.name}"
                )

            sale_details.append(
                SaleDetail(
                    product_id = product.id,
                    quantity = detail.quantity,
                    unit_price = product.price,
                    subtotal = product.price * detail.quantity
                )
            )

        return sale_details

    @staticmethod
    def discount_stock(details, db: Session):
        # Descontamos las piezas vendidas del inventario
        for detail in details:
            product = ProductRepository.find_product(product_id = detail.product_id, db = db)
            product.stock -= detail.quantity
            product.updated_at = datetime.now(timezone.utc)

    @staticmethod
    def restore_stock(details, db: Session):
        # Regresamos piezas al inventario al modificar o eliminar una venta
        for detail in details:
            product = ProductRepository.find_product(product_id = detail.product_id, db = db)

            if product:
                product.stock += detail.quantity
                product.updated_at = datetime.now(timezone.utc)
