from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status
from config.database import get_db
from dtos.client.client_create import ClientCreateDTO
from dtos.client.client_response import ClientResponseDTO
from dtos.client.client_update import ClientUpdateDTO
from services.client_service import ClientService

# Router de clientes
router = APIRouter(
    prefix = "/clients",
    tags = ["Clients"]
)

# Endpoints del CRUD
@router.get("/", response_model = List[ClientResponseDTO], status_code = status.HTTP_200_OK)
def get_clients(db: Session = Depends(get_db)):
    return ClientService.get_clients(db = db)

@router.get("/{client_id}", response_model = ClientResponseDTO, status_code = status.HTTP_200_OK)
def find_client(client_id: int, db: Session = Depends(get_db)):
    return ClientService.find_client(client_id = client_id, db = db)

@router.post("/", response_model = ClientResponseDTO, status_code = status.HTTP_201_CREATED)
def create_client(data: ClientCreateDTO, db: Session = Depends(get_db)):
    return ClientService.create_client(dto = data, db = db)

@router.put("/", response_model = ClientResponseDTO, status_code = status.HTTP_202_ACCEPTED)
def update_client(data: ClientUpdateDTO, db: Session = Depends(get_db)):
    return ClientService.update_client(dto = data, db = db)

@router.delete("/{client_id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_client(client_id: int, db: Session = Depends(get_db)):
    ClientService.delete_client(client_id = client_id, db = db)
