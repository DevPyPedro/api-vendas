import pandas as pd #type: ignore
import logging

from src.infraestructure.database.interfaces.conn_repository_interface import IDatabaseRepository
from src.infraestructure.database.settings.conn import PGconnectionHandler

class DatabaseRepository(IDatabaseRepository):
    
    @classmethod
    def run_query(cls, query: str, will_return: bool = False):
        try:
            db_handler = PGconnectionHandler()
            with db_handler as conn:
                if will_return:
                    for q in query:
                        df = pd.read_sql(q, conn)
                        conn.commit()
                    return df
                
                else:
                    cursor = conn.cursor()
                    for q in query:
                        cursor.execute(q)
                        conn.commit()
                    return True
                
        except Exception as e:
            print(f'Erro ao executar a query: {query}: {e}')
            logging.error(f"\nErro ao executar a query: {query}: {e}\n")