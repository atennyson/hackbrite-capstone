import psycopg2
import pandas as pd
import os
import dotenv


dotenv.load_dotenv("secrets.env")

name = os.getenv("DBNAME")
user = os.getenv("DBUSER")
password = os.getenv("DBPASS")
port = os.getenv("DBPORT")


def make_connection(name, user, password, port):
    con = psycopg2.connect(f"dbname={name} user={user} password={password} port={port}")

    return con


def db_query(c, q):
    rows = pd.read_sql_query(q, c)
    c.close()
    return rows
