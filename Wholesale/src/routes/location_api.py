from fastapi import APIRouter
from starlette import status
from typing import List
from services.location_service import LocationService
from dtos.location.location_response import LocationResponseDTO
from dtos.location.location_create import LocationCreateDTO
from dtos.location.location_update import LocationUpdateDTO

# Router de sucursales
router = APIRouter(
    prefix = "/locations",
    tags = ["Locations"]
)

# Endpoints del CRUD
@router.get("/", response_model = List[LocationResponseDTO], status_code = status.HTTP_200_OK)
def get_locations():
    return LocationService.get_locations()

@router.get("/{location_id}", response_model = LocationResponseDTO, status_code = status.HTTP_200_OK)
def find_location(location_id: int):
    return LocationService.find_location(location_id = location_id)

@router.post("/", response_model = LocationResponseDTO, status_code = status.HTTP_201_CREATED)
def create_location(data: LocationCreateDTO):
    return LocationService.create_location(dto = data)

@router.put("/", response_model = LocationResponseDTO, status_code = status.HTTP_202_ACCEPTED)
def update_location(data: LocationUpdateDTO):
    return LocationService.update_location(dto = data)

@router.delete("/{location_id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_location(location_id: int):
    LocationService.delete_location(location_id = location_id)
