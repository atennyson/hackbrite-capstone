import psycopg2
import pandas as pd
import os
import dotenv


dotenv.load_dotenv("secrets.env")

name = os.getenv("DBNAME")
user = os.getenv("DBUSER")
password = os.getenv("DBPASS")
port = os.getenv("DBPORT")


con = psycopg2.connect(f"dbname={name} user={user} password={password} port={port}")

cur = con.cursor()


def db_query(c, q):
    rows = pd.read_sql_query(q, c)
    cur.close()
    con.close()
    return rows
