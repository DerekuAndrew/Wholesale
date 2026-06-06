from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status
from config.database import get_db
from dtos.location.location_create import LocationCreateDTO
from dtos.location.location_response import LocationResponseDTO
from dtos.location.location_update import LocationUpdateDTO
from services.location_service import LocationService

# Router de sucursales
router = APIRouter(
    prefix = "/locations",
    tags = ["Locations"]
)

# Endpoints del CRUD
@router.get("/", response_model = List[LocationResponseDTO], status_code = status.HTTP_200_OK)
def get_locations(db: Session = Depends(get_db)):
    return LocationService.get_locations(db = db)

@router.get("/{location_id}", response_model = LocationResponseDTO, status_code = status.HTTP_200_OK)
def find_location(location_id: int, db: Session = Depends(get_db)):
    return LocationService.find_location(location_id = location_id, db = db)

@router.post("/", response_model = LocationResponseDTO, status_code = status.HTTP_201_CREATED)
def create_location(data: LocationCreateDTO, db: Session = Depends(get_db)):
    return LocationService.create_location(dto = data, db = db)

@router.put("/", response_model = LocationResponseDTO, status_code = status.HTTP_202_ACCEPTED)
def update_location(data: LocationUpdateDTO, db: Session = Depends(get_db)):
    return LocationService.update_location(dto = data, db = db)

@router.delete("/{location_id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_location(location_id: int, db: Session = Depends(get_db)):
    LocationService.delete_location(location_id = location_id, db = db)
