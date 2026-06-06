from datetime import datetime, timezone
from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status
from dtos.client.client_create import ClientCreateDTO
from dtos.client.client_update import ClientUpdateDTO
from models.client import Client
from repositories.client_repository import ClientRepository

class ClientService:
    @staticmethod
    def get_clients(db: Session):
        return ClientRepository.get_clients(db = db)

    @staticmethod
    def find_client(client_id: int, db: Session):
        client = ClientRepository.find_client(client_id = client_id, db = db)

        if not client:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Client not found"
            )

        return client

    @staticmethod
    def create_client(dto: ClientCreateDTO, db: Session):
        # Armamos el cliente que se va a guardar
        now = datetime.now(timezone.utc)
        data = Client(
            name = dto.name,
            phone = dto.phone,
            email = dto.email,
            rfc = dto.rfc,
            active = True,
            created_at = now,
            updated_at = now
        )

        return ClientRepository.create_client(data = data, db = db)

    @staticmethod
    def update_client(dto: ClientUpdateDTO, db: Session):
        # Armamos el cliente con los datos actualizados
        data = Client(
            id = dto.id,
            name = dto.name,
            phone = dto.phone,
            email = dto.email,
            rfc = dto.rfc,
            updated_at = datetime.now(timezone.utc)
        )

        client = ClientRepository.update_client(data = data, db = db)

        if not client:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Client not found"
            )

        return client

    @staticmethod
    def delete_client(client_id: int, db: Session):
        client = ClientRepository.delete_client(
            client_id = client_id,
            updated_at = datetime.now(timezone.utc),
            db = db
        )

        if not client:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Client not found"
            )

        return client
