from abc import abstractmethod, ABC

class IClientRepository(ABC):
     
    def get_all_client()->list:
        '''Retorna todos os clientes'''