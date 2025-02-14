import pytest

from src.infraestructure.database.settings.conn import PGconnectionHandler

def test_conn():

    conn = PGconnectionHandler()

    get_conn_test = conn.get_conn()

    assert get_conn_test is not None # Validando se a conexão retorna None