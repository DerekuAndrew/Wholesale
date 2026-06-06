from sqlalchemy.orm import Session
from models.product import Product

class ProductRepository:
    @staticmethod
    def get_products(db: Session):
        products = db.query(Product).filter(
            Product.active == True
        ).all()
        return products

    @staticmethod
    def find_product(product_id: int, db: Session):
        product = db.query(Product).filter(Product.id == product_id).first()
        return product

    @staticmethod
    def find_product_by_barcode(barcode: str, db: Session):
        product = db.query(Product).filter(Product.barcode == barcode).first()
        return product

    @staticmethod
    def create_product(data: Product, db: Session):
        db.add(data)
        db.commit()
        db.refresh(data)
        return data

    @staticmethod
    def update_product(data: Product, db: Session):
        product = ProductRepository.find_product(product_id = data.id, db = db)

        if product is None:
            return None

        product.barcode = data.barcode
        product.name = data.name
        product.description = data.description
        product.brand = data.brand
        product.price = data.price
        product.stock = data.stock
        product.updated_at = data.updated_at

        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    def delete_product(product_id: int, updated_at, db: Session):
        product = ProductRepository.find_product(product_id = product_id, db = db)

        if product is None:
            return None

        product.active = False
        product.updated_at = updated_at
        db.commit()
        db.refresh(product)
        return product
