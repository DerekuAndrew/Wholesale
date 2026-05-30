from fastapi import HTTPException
from starlette import status
from datetime import datetime, timezone
from dtos.location.location_response import LocationResponseDTO
from dtos.location.location_create import LocationCreateDTO
from dtos.location.location_update import LocationUpdateDTO
from services.client_service import ClientService

# Datos simulados por el momento
from simulations.locations_data import locations_data
locations = locations_data

class LocationService:

    @staticmethod
    def get_locations():
        active_locations = [l for l in locations if l.active]
        return active_locations

    @staticmethod
    def find_location(location_id: int):
        location: LocationResponseDTO = next((l for l in locations if l.id == location_id), None)

        if not location:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Location not found"
            )

        return location

    @staticmethod
    def create_location(dto: LocationCreateDTO):
        # Sacamos el siguiente id disponible
        location_id = max((l.id for l in locations), default = 0) + 1

        # Revisamos que el cliente exista
        ClientService.find_client(client_id = dto.client_id)

        # Tomamos la fecha actual
        now = datetime.now(timezone.utc)

        # Creamos la sucursal
        location = LocationResponseDTO(
            id = location_id,
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

        # Agregamos la sucursal a la lista
        locations.append(location)

        # Regresamos el resultado
        return location

    @staticmethod
    def update_location(dto: LocationUpdateDTO):
        # Buscamos la sucursal
        location: LocationResponseDTO = LocationService.find_location(location_id = dto.id)

        # Revisamos que el cliente exista
        ClientService.find_client(client_id = dto.client_id)

        # Actualizamos los datos
        location.name = dto.name
        location.address = dto.address
        location.city = dto.city
        location.state = dto.state
        location.postal_code = dto.postal_code
        location.phone = dto.phone
        location.email = dto.email
        location.updated_at = datetime.now(timezone.utc)

        return location

    @staticmethod
    def delete_location(location_id: int):
        location: LocationResponseDTO = LocationService.find_location(location_id = location_id)

        location.active = False
        location.updated_at = datetime.now(timezone.utc)

        return location
