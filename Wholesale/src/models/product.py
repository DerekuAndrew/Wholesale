from sqlalchemy import Boolean, Column, DateTime, Integer, Numeric, String
from sqlalchemy.orm import relationship
from config.database import Base

class Product(Base):
    __tablename__ = "Products"

    id = Column(
        "ProductId",
        Integer,
        primary_key=True,
        index=True
    )

    barcode = Column(
        "ProductBarcode",
        String(50),
        nullable=False,
        unique=True
    )

    name = Column(
        "ProductName",
        String(250),
        nullable=False
    )

    description = Column(
        "ProductDescription",
        String(250),
        nullable=True
    )

    brand = Column(
        "ProductBrand",
        String(100),
        nullable=False
    )

    price = Column(
        "ProductPrice",
        Numeric(16, 2),
        nullable=False
    )

    stock = Column(
        "ProductStock",
        Integer,
        nullable=False
    )

    active = Column(
        "ProductActive",
        Boolean,
        nullable=False
    )

    created_at = Column(
        "ProductCreatedAt",
        DateTime,
        nullable=False
    )

    updated_at = Column(
        "ProductUpdatedAt",
        DateTime,
        nullable=False
    )

    # Relacion con los detalles de venta
    sale_details = relationship(
        "SaleDetail",
        back_populates="product"
    )
