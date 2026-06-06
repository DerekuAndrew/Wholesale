from datetime import datetime, timezone
from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status
from dtos.location.location_create import LocationCreateDTO
from dtos.location.location_update import LocationUpdateDTO
from models.location import Location
from repositories.location_repository import LocationRepository

class LocationService:
    @staticmethod
    def get_locations(db: Session):
        return LocationRepository.get_locations(db = db)

    @staticmethod
    def find_location(location_id: int, db: Session):
        location = LocationRepository.find_location(location_id = location_id, db = db)

        if not location:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Location not found"
            )

        return location

    @staticmethod
    def create_location(dto: LocationCreateDTO, db: Session):
        # Armamos la sucursal que se va a guardar
        now = datetime.now(timezone.utc)
        data = Location(
            client_id = dto.client_id,
            name = dto.name,
            address = dto.address,
            city = dto.city,
            state = dto.state,
            postal_code = dto.postal_code,
            phone = dto.phone,
            email = dto.email,
            active = True,
            created_at = now,
            updated_at = now
        )

        return LocationRepository.create_location(data = data, db = db)

    @staticmethod
    def update_location(dto: LocationUpdateDTO, db: Session):
        # Armamos la sucursal con los datos actualizados
        data = Location(
            id = dto.id,
            client_id = dto.client_id,
            name = dto.name,
            address = dto.address,
            city = dto.city,
            state = dto.state,
            postal_code = dto.postal_code,
            phone = dto.phone,
            email = dto.email,
            updated_at = datetime.now(timezone.utc)
        )

        location = LocationRepository.update_location(data = data, db = db)

        if not location:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Location not found"
            )

        return location

    @staticmethod
    def delete_location(location_id: int, db: Session):
        location = LocationRepository.delete_location(
            location_id = location_id,
            updated_at = datetime.now(timezone.utc),
            db = db
        )

        if not location:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Location not found"
            )

        return location
