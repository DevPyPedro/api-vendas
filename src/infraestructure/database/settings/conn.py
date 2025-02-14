from typing import Optional
import psycopg2 # type: ignore

from src.infraestructure.config.database import configPG

class PGconnectionHandler:
    def __init__(self) -> None:
        self.__conn_pg = None
        self.__config_pg = {
            "database": configPG["database"],
            "user": configPG["user"],
            "host": configPG["host"],
            "password": configPG["password"],
            "port": configPG["port"]
            
        }
        print(self.__config_pg)

    def __create_conn_pg(self) -> Optional[psycopg2.extensions.connection]:
        '''Criando conexão com o Postgre'''
        try:
            self.__conn_pg = psycopg2.connect(
                dbname=configPG["database"],
                user=configPG["user"],
                password=configPG["password"],
                host=configPG["host"],
                port=configPG["port"],
                client_encoding="UTF8"  # Forçar UTF-8, client_encoding="UTF8"
            )

            return self.__conn_pg
        except Exception as e:
            print(f"Error connecting to PostgreSQL: {e}")
            return None

    def get_conn(self) -> Optional[psycopg2.extensions.connection]:
        if self.__conn_pg is None:
            return self.__create_conn_pg()
        return self.__conn_pg
    
    def __enter__(self)-> Optional[psycopg2.extensions.connection]:
        return self.get_conn()

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.__conn_pg:
            self.__conn_pg.close()
            self.__conn_pg = None