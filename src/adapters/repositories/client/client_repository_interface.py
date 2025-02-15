from abc import abstractmethod, ABC

class IClientRepository(ABC):
     
    @abstractmethod
    def get_all_client()->list:
        '''Retorna todos os clientes'''

    @abstractmethod
    def get_client_by_id(self, idcliente: int)->dict:
        '''Retornda um cliente pelo id '''