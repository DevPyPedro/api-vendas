import os
from dotenv import load_dotenv

load_dotenv(".env")

configPG = {
    "database"  : str(os.getenv("PGDATABASE")),
    "user"      : str(os.getenv("PGUSER")),
    "host"      : str(os.getenv("PGHOST")),
    "password"  : str(os.getenv("PGPASSWORD")),
    "port"      : int(os.getenv("PGPORT")),
}