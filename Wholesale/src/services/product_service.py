from datetime import datetime, timezone
from fastapi import HTTPException
from starlette import status
from dtos.product.product_create import ProductCreateDTO
from dtos.product.product_response import ProductResponseDTO
from dtos.product.product_update import ProductUpdateDTO
from simulations.products_data import products_data

# Datos simulados por el momento
products = products_data

class ProductService:
    @staticmethod
    def get_products():
        # Regresamos solo los productos activos
        return [p for p in products if p.active]

    @staticmethod
    def find_product(product_id: int):
        # Buscamos el producto por su id
        product: ProductResponseDTO = next((p for p in products if p.id == product_id), None)

        if not product or not product.active:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found"
            )

        return product

    @staticmethod
    def create_product(dto: ProductCreateDTO):
        # Validamos que no se repita el codigo de barras
        ProductService.validate_barcode(dto.barcode)

        product_id = max((p.id for p in products), default=0) + 1
        now = datetime.now(timezone.utc)

        product = ProductResponseDTO(
            id=product_id,
            barcode=dto.barcode,
            name=dto.name,
            description=dto.description,
            brand=dto.brand,
            price=dto.price,
            stock=dto.stock,
            active=True,
            created_at=now,
            updated_at=now
        )

        products.append(product)
        return product

    @staticmethod
    def update_product(dto: ProductUpdateDTO):
        # Actualizamos el producto despues de revisar el codigo de barras
        product: ProductResponseDTO = ProductService.find_product(product_id=dto.id)
        ProductService.validate_barcode(dto.barcode, product_id=dto.id)

        product.barcode = dto.barcode
        product.name = dto.name
        product.description = dto.description
        product.brand = dto.brand
        product.price = dto.price
        product.stock = dto.stock
        product.updated_at = datetime.now(timezone.utc)

        return product

    @staticmethod
    def delete_product(product_id: int):
        # Lo desactivamos para no perder referencias de ventas
        product: ProductResponseDTO = ProductService.find_product(product_id=product_id)
        product.active = False
        product.updated_at = datetime.now(timezone.utc)

        return product

    @staticmethod
    def validate_barcode(barcode: str, product_id: int = None):
        # Revisamos que no haya otro producto activo con el mismo codigo
        existing_product = next(
            (p for p in products if p.barcode == barcode and p.active and p.id != product_id),
            None
        )

        if existing_product:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Product barcode already exists"
            )
