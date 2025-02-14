from src.infraestructure.database.repositories.client_repository import ClientRepository
from src.infraestructure.database.repositories.conn_repository import DatabaseRepository
from src.app.use_case.client.client_use_case import ClientUseCase

def get_client_depends()->ClientUseCase:
    return ClientUseCase(ClientRepository(DatabaseRepository()))