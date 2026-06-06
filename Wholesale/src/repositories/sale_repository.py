from sqlalchemy.orm import Session, joinedload
from models.sale import Sale
from models.sale_detail import SaleDetail

class SaleRepository:
    @staticmethod
    def get_sales(db: Session):
        sales = db.query(Sale).options(
            joinedload(Sale.details)
        ).filter(
            Sale.status != "DELETED"
        ).all()
        return sales

    @staticmethod
    def find_sale(sale_id: int, db: Session):
        sale = db.query(Sale).options(
            joinedload(Sale.details)
        ).filter(Sale.id == sale_id).first()
        return sale

    @staticmethod
    def create_sale(data: Sale, db: Session):
        db.add(data)
        db.flush()
        data.folio = SaleRepository.create_folio(data.id)
        db.commit()
        db.refresh(data)
        return data

    @staticmethod
    def update_sale(data: Sale, details: list[SaleDetail], db: Session):
        sale = SaleRepository.find_sale(sale_id = data.id, db = db)

        if sale is None:
            return None

        sale.location_id = data.location_id
        sale.total = data.total
        sale.status = data.status
        sale.updated_at = data.updated_at
        sale.details = details

        db.commit()
        db.refresh(sale)
        return sale

    @staticmethod
    def delete_sale(sale_id: int, updated_at, db: Session):
        sale = SaleRepository.find_sale(sale_id = sale_id, db = db)

        if sale is None:
            return None

        sale.status = "DELETED"
        sale.updated_at = updated_at
        db.commit()
        db.refresh(sale)
        return sale

    @staticmethod
    def create_folio(sale_id: int):
        return f"SALE-{sale_id:04d}"
