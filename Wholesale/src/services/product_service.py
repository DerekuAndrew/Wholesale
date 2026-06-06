from datetime import datetime, timezone
from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status
from dtos.product.product_create import ProductCreateDTO
from dtos.product.product_update import ProductUpdateDTO
from models.product import Product
from repositories.product_repository import ProductRepository

class ProductService:
    @staticmethod
    def get_products(db: Session):
        return ProductRepository.get_products(db = db)

    @staticmethod
    def find_product(product_id: int, db: Session):
        # Buscamos el producto y revisamos que siga activo
        product = ProductRepository.find_product(product_id = product_id, db = db)

        if not product or not product.active:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Product not found"
            )

        return product

    @staticmethod
    def create_product(dto: ProductCreateDTO, db: Session):
        # Validamos que no exista otro producto con ese codigo
        ProductService.validate_barcode(barcode = dto.barcode, db = db)

        now = datetime.now(timezone.utc)
        data = Product(
            barcode = dto.barcode,
            name = dto.name,
            description = dto.description,
            brand = dto.brand,
            price = dto.price,
            stock = dto.stock,
            active = True,
            created_at = now,
            updated_at = now
        )

        return ProductRepository.create_product(data = data, db = db)

    @staticmethod
    def update_product(dto: ProductUpdateDTO, db: Session):
        # Armamos el producto con los datos que llegan del request
        ProductService.find_product(product_id = dto.id, db = db)
        ProductService.validate_barcode(barcode = dto.barcode, db = db, product_id = dto.id)

        data = Product(
            id = dto.id,
            barcode = dto.barcode,
            name = dto.name,
            description = dto.description,
            brand = dto.brand,
            price = dto.price,
            stock = dto.stock,
            updated_at = datetime.now(timezone.utc)
        )

        product = ProductRepository.update_product(data = data, db = db)

        if not product:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Product not found"
            )

        return product

    @staticmethod
    def delete_product(product_id: int, db: Session):
        # Lo desactivamos para conservar referencias de ventas
        ProductService.find_product(product_id = product_id, db = db)
        product = ProductRepository.delete_product(
            product_id = product_id,
            updated_at = datetime.now(timezone.utc),
            db = db
        )

        if not product:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Product not found"
            )

        return product

    @staticmethod
    def validate_barcode(barcode: str, db: Session, product_id: int = None):
        product = ProductRepository.find_product_by_barcode(barcode = barcode, db = db)

        if product and product.id != product_id:
            raise HTTPException(
                status_code = status.HTTP_409_CONFLICT,
                detail = "Product barcode already exists"
            )
