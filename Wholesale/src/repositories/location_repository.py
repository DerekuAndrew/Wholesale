from sqlalchemy.orm import Session
from models.location import Location
from services.client_service import ClientService

class LocationRepository:
    @staticmethod
    def get_locations(db: Session):
        locations = db.query(Location).filter(
            Location.active == True
        ).all()
        return locations

    @staticmethod
    def find_location(location_id: int, db: Session):
        location = db.query(Location).filter(Location.id == location_id).first()
        return location

    @staticmethod
    def create_location(data: Location, db: Session):
        # Revisamos que el cliente exista
        ClientService.find_client(client_id = data.client_id, db = db)

        db.add(data)
        db.commit()
        db.refresh(data)
        return data

    @staticmethod
    def update_location(data: Location, db: Session):
        # Revisamos que el cliente y la sucursal existan
        ClientService.find_client(client_id = data.client_id, db = db)
        location = LocationRepository.find_location(location_id = data.id, db = db)

        if location is None:
            return None

        location.client_id = data.client_id
        location.name = data.name
        location.address = data.address
        location.city = data.city
        location.state = data.state
        location.postal_code = data.postal_code
        location.phone = data.phone
        location.email = data.email

        db.commit()
        db.refresh(location)
        return location

    @staticmethod
    def delete_location(location_id: int, updated_at, db: Session):
        location = LocationRepository.find_location(location_id = location_id, db = db)

        if location is None:
            return None

        location.active = False
        location.updated_at = updated_at

        db.commit()
        db.refresh(location)
        return location
