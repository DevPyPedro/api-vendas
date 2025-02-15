from src.adapters.repositories.client.client_repository_interface import  IClientRepository

class ClientUseCase:

    def __init__(self, client: IClientRepository):
        self.client = client

    def execute(self, idcliente: int =None):
        '''Caso de uso do cliente'''
        response = self.client.get_all_client() if idcliente is None else self.client.get_client_by_id(idcliente)
        return {"status": True if response else False, "data": response }