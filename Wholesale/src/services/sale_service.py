from datetime import datetime, timezone
from fastapi import HTTPException
from starlette import status
from dtos.sale.sale_create import SaleCreateDTO
from dtos.sale.sale_response import SaleResponseDTO
from dtos.sale.sale_update import SaleUpdateDTO
from dtos.sale_detail.sale_detail_response import SaleDetailResponseDTO
from services.location_service import LocationService
from services.product_service import ProductService
from simulations.sales_data import sales_data

# Datos simulados por el momento
sales = sales_data

class SaleService:
    @staticmethod
    def get_sales():
        # Regresamos las ventas que no esten eliminadas
        return [s for s in sales if s.status != "DELETED"]

    @staticmethod
    def find_sale(sale_id: int):
        # Buscamos la venta por su id
        sale: SaleResponseDTO = next((s for s in sales if s.id == sale_id), None)

        if not sale or sale.status == "DELETED":
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Sale not found"
            )

        return sale

    @staticmethod
    def create_sale(dto: SaleCreateDTO):
        # Validamos la sucursal y armamos los detalles con los precios actuales
        LocationService.find_location(location_id=dto.location_id)

        sale_id = max((s.id for s in sales), default=0) + 1
        now = datetime.now(timezone.utc)
        details = SaleService.build_details(sale_id=sale_id, details=dto.details)
        total = sum(d.subtotal for d in details)

        sale = SaleResponseDTO(
            id=sale_id,
            folio=SaleService.create_folio(sale_id),
            location_id=dto.location_id,
            datetime=now,
            total=total,
            status=dto.status,
            created_at=now,
            updated_at=now,
            details=details
        )

        sales.append(sale)
        SaleService.discount_stock(details)
        return sale

    @staticmethod
    def update_sale(dto: SaleUpdateDTO):
        # Regresamos el stock anterior antes de cambiar los detalles
        sale: SaleResponseDTO = SaleService.find_sale(sale_id=dto.id)
        LocationService.find_location(location_id=dto.location_id)
        SaleService.restore_stock(sale.details)

        try:
            details = SaleService.build_details(sale_id=sale.id, details=dto.details)
        except HTTPException:
            SaleService.discount_stock(sale.details)
            raise

        sale.location_id = dto.location_id
        sale.total = sum(d.subtotal for d in details)
        sale.status = dto.status
        sale.details = details
        sale.updated_at = datetime.now(timezone.utc)

        SaleService.discount_stock(details)
        return sale

    @staticmethod
    def delete_sale(sale_id: int):
        # Marcamos la venta como eliminada y regresamos el stock
        sale: SaleResponseDTO = SaleService.find_sale(sale_id=sale_id)
        SaleService.restore_stock(sale.details)
        sale.status = "DELETED"
        sale.updated_at = datetime.now(timezone.utc)

        return sale

    @staticmethod
    def build_details(sale_id: int, details):
        # Convertimos los productos solicitados en renglones de venta
        sale_details = []
        requested_stock = {}
        next_detail_id = SaleService.next_detail_id()

        for index, detail in enumerate(details):
            product = ProductService.find_product(product_id=detail.product_id)
            requested_stock[product.id] = requested_stock.get(product.id, 0) + detail.quantity

            if product.stock < requested_stock[product.id]:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Insufficient stock for product {product.name}"
                )

            subtotal = product.price * detail.quantity
            sale_details.append(
                SaleDetailResponseDTO(
                    id=next_detail_id + index,
                    sale_id=sale_id,
                    product_id=product.id,
                    quantity=detail.quantity,
                    unit_price=product.price,
                    subtotal=subtotal
                )
            )

        return sale_details

    @staticmethod
    def discount_stock(details):
        # Descontamos del inventario las piezas vendidas
        for detail in details:
            product = ProductService.find_product(product_id=detail.product_id)
            product.stock -= detail.quantity
            product.updated_at = datetime.now(timezone.utc)

    @staticmethod
    def restore_stock(details):
        # Regresamos piezas al inventario cuando se modifica o elimina una venta
        for detail in details:
            product = ProductService.find_product(product_id=detail.product_id)
            product.stock += detail.quantity
            product.updated_at = datetime.now(timezone.utc)

    @staticmethod
    def create_folio(sale_id: int):
        # Generamos un folio sencillo para identificar la venta
        return f"SALE-{sale_id:04d}"

    @staticmethod
    def next_detail_id():
        # Continuamos los ids de detalle despues del ultimo registrado
        detail_ids = [d.id for sale in sales for d in sale.details]
        return max(detail_ids, default=0) + 1
