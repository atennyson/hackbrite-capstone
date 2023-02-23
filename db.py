import pandas as pd
import os
import dotenv
from sqlalchemy import create_engine


dotenv.load_dotenv("secrets.env")

host = os.getenv("DBHOST")
name = os.getenv("DBNAME")
user = os.getenv("DBUSER")
password = os.getenv("DBPASS")
port = os.getenv("DBPORT")


def make_connection(host, name, user, password, port):
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{name}')

    con = engine.connect()

    return con


def db_query(c, q):
    rows = pd.read_sql_query(q, c)
    c.close()
    return rows
