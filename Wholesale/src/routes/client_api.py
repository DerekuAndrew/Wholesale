from fastapi import APIRouter
from starlette import status
from typing import List
from services.client_service import ClientService
from dtos.client.client_response import ClientResponseDTO
from dtos.client.client_create import ClientCreateDTO
from dtos.client.client_update import ClientUpdateDTO

# Router de clientes
router = APIRouter(
    prefix = "/clients",
    tags = ["Clients"]
)

# Endpoints del CRUD
@router.get("/", response_model = List[ClientResponseDTO], status_code = status.HTTP_200_OK)
def get_clients():
    return ClientService.get_clients()

@router.get("/{client_id}", response_model = ClientResponseDTO, status_code = status.HTTP_200_OK)
def find_client(client_id: int):
    return ClientService.find_client(client_id = client_id)

@router.post("/", response_model = ClientResponseDTO, status_code = status.HTTP_201_CREATED)
def create_client(data: ClientCreateDTO):
    return ClientService.create_client(dto = data)

@router.put("/", response_model = ClientResponseDTO, status_code = status.HTTP_202_ACCEPTED)
def update_client(data: ClientUpdateDTO):
    return ClientService.update_client(dto = data)

@router.delete("/{client_id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_client(client_id: int):
    ClientService.delete_client(client_id = client_id)
