from fastapi import HTTPException
from starlette import status
from datetime import datetime, timezone
from dtos.client.client_response import ClientResponseDTO
from dtos.client.client_create import ClientCreateDTO
from dtos.client.client_update import ClientUpdateDTO

# Datos simulados por el momento
from simulations.clients_data import clients_data
clients = clients_data

class ClientService:

    @staticmethod
    def get_clients():
        active_clients = [c for c in clients if c.active]
        return active_clients

    @staticmethod
    def find_client(client_id: int):
        client: ClientResponseDTO = next((c for c in clients if c.id == client_id), None)

        if not client:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = "Client not found"
            )

        return client

    @staticmethod
    def create_client(dto: ClientCreateDTO):
        # Sacamos el siguiente id disponible
        client_id = max((c.id for c in clients), default = 0) + 1

        # Tomamos la fecha actual
        now = datetime.now(timezone.utc)

        # Creamos el cliente
        client = ClientResponseDTO(
            id = client_id,
            name = dto.name,
            phone = dto.phone,
            email = dto.email,
            rfc = dto.rfc,
            active = True,
            created_at = now,
            updated_at = now
        )

        # Agregamos el cliente a la lista
        clients.append(client)

        # Regresamos el resultado
        return client

    @staticmethod
    def update_client(dto: ClientUpdateDTO):
        # Buscamos el cliente
        client: ClientResponseDTO = ClientService.find_client(client_id = dto.id)

        # Actualizamos los datos
        client.name = dto.name
        client.phone = dto.phone
        client.email = dto.email
        client.rfc = dto.rfc
        client.updated_at = datetime.now(timezone.utc)

        return client

    @staticmethod
    def delete_client(client_id: int):
        client: ClientResponseDTO = ClientService.find_client(client_id = client_id)

        client.active = False
        client.updated_at = datetime.now(timezone.utc)

        return client
