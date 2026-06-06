from sqlalchemy import Column, ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship
from config.database import Base

class SaleDetail(Base):
    __tablename__ = "SaleDetails"

    id = Column(
        "SaleDetailId",
        Integer,
        primary_key=True,
        index=True
    )

    sale_id = Column(
        "SaleId",
        Integer,
        ForeignKey("Sales.SaleId"),
        nullable=False
    )

    product_id = Column(
        "ProductId",
        Integer,
        ForeignKey("Products.ProductId"),
        nullable=False
    )

    quantity = Column(
        "SaleDetailQuantity",
        Integer,
        nullable=False
    )

    unit_price = Column(
        "SaleDetailUnitPrice",
        Numeric(16, 2),
        nullable=False
    )

    subtotal = Column(
        "SaleDetailSubtotal",
        Numeric(16, 2),
        nullable=False
    )

    # Relacion con la venta
    sale = relationship(
        "Sale",
        back_populates="details"
    )

    # Relacion con el producto
    product = relationship(
        "Product",
        back_populates="sale_details"
    )
