from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship
from config.database import Base

class Sale(Base):
    __tablename__ = "Sales"

    id = Column(
        "SaleId",
        Integer,
        primary_key=True,
        index=True
    )

    folio = Column(
        "SaleFolio",
        String(50),
        nullable=False,
        unique=True
    )

    location_id = Column(
        "LocationId",
        Integer,
        ForeignKey("Locations.locationId"),
        nullable=False
    )

    datetime = Column(
        "SaleDatetime",
        DateTime,
        nullable=False
    )

    total = Column(
        "SaleTotal",
        Numeric(16, 2),
        nullable=False
    )

    status = Column(
        "SaleStatus",
        String(50),
        nullable=False
    )

    created_at = Column(
        "SaleCreatedAt",
        DateTime,
        nullable=False
    )

    updated_at = Column(
        "SaleUpdatedAt",
        DateTime,
        nullable=False
    )

    # Relacion con la sucursal
    location = relationship(
        "Location",
        back_populates="sales"
    )

    # Relacion con los productos vendidos
    details = relationship(
        "SaleDetail",
        back_populates="sale",
        cascade="all, delete-orphan"
    )
