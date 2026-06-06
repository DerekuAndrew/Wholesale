from sqlalchemy.orm import Session, joinedload, with_loader_criteria
from models.client import Client
from models.location import Location

class ClientRepository:
    @staticmethod
    def get_clients(db: Session):
        clients = db.query(Client).options(
            joinedload(Client.locations),
            with_loader_criteria(
                Location,
                Location.active == True
            )
        ).filter(
            Client.active == True
        ).all()
        return clients

    @staticmethod
    def find_client(client_id: int, db: Session):
        client = db.query(Client).filter(Client.id == client_id).first()
        return client

    @staticmethod
    def create_client(data: Client, db: Session):
        db.add(data)
        db.commit()
        db.refresh(data)
        return data

    @staticmethod
    def update_client(data: Client, db: Session):
        client = ClientRepository.find_client(client_id = data.id, db = db)

        if client is None:
            return None

        client.name = data.name
        client.phone = data.phone
        client.email = data.email
        client.rfc = data.rfc
        client.updated_at = data.updated_at

        db.commit()
        db.refresh(client)
        return client

    @staticmethod
    def delete_client(client_id: int, updated_at, db: Session):
        client = ClientRepository.find_client(client_id = client_id, db = db)

        if client is None:
            return None

        client.active = False
        client.updated_at = updated_at

        db.commit()
        db.refresh(client)
        return client
