from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base

class Location(Base):
    __tablename__ = "Locations"

    id = Column(
        "locationId",
        Integer,
        primary_key=True,
        index=True
    )

    client_id = Column(
        "ClientId",
        Integer,
        ForeignKey("Clients.ClientId"),
        nullable=False
    )

    name = Column(
        "LocationName",
        String(250),
        nullable=False
    )

    address = Column(
        "LocationAddress",
        String(250),
        nullable=False
    )

    city = Column(
        "LocationCity",
        String(100),
        nullable=False
    )

    state = Column(
        "LocationState",
        String(100),
        nullable=False
    )

    postal_code = Column(
        "LocationPostalCode",
        String(50),
        nullable=False
    )

    phone = Column(
        "LocationPhone",
        String(10),
        nullable=True
    )

    email = Column(
        "LocationEmail",
        String(100),
        nullable=True
    )

    active = Column(
        "LocationActive",
        Boolean,
        nullable=False
    )

    created_at = Column(
        "LocationCreatedAt",
        DateTime,
        nullable=False
    )

    updated_at = Column(
        "LocationUpdatedAt",
        DateTime,
        nullable=False
    )

    # Relacion con el cliente
    client = relationship(
        "Client",
        back_populates="locations"
    )

    # Relacion con las ventas
    sales = relationship(
        "Sale",
        back_populates="location"
    )
