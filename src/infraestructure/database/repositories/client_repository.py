import pandas as pd

from src.adapters.repositories.client.client_repository_interface import IClientRepository
from src.infraestructure.database.interfaces.conn_repository_interface import IDatabaseRepository

class ClientRepository(IClientRepository):
    def __init__(self, conn: IDatabaseRepository):
        self.conn = conn

    def get_all_client(self)->dict:
        '''Retorna todos os clientes'''
        query = '''select * from relacional.clientes'''
        result = self.conn.run_query(query=[query], will_return=True)
        result_dict = result.to_dict("records")
        return result_dict
    
    def get_client_by_id(self, idcliente: int)->dict:
        '''Retornda um cliente pelo id '''
        query = f'''select * from relacional.clientes as cliente where cliente.idcliente ={idcliente}'''
        result = self.conn.run_query(query=[query], will_return=True)
        result_dict = result.to_dict("records")
        return result_dict