from src.adapters.repositories.client.client_repository_interface import  IClientRepository

class ClientUseCase:

    def __init__(self, client: IClientRepository):
        self.client =client

    def execute(self):
        '''Caso de uso do cliente'''
        response = self.client.get_all_client()
        return {"status": True if response else False, "data": response }