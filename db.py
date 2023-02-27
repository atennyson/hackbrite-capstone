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


def make_connection():
    """Creates an engine object using a database connect string. Uses the connect() method on the engine object to
    create an engine.connect object (connection to the database)

    :return: engine.connect object - connection to the database
    """

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{name}')

    con = engine.connect()

    return con


def db_query(con, query):
    """
    Sends a query to the database and returns a Dataframe object

    :param con: engine.connect object - same object returned from make_connection()
    :param query: string - sql query from user input
    :return: Dataframe - Dataframe created from read_sql_query function from the pandas module
    """
    rows = pd.read_sql_query(query, con)
    con.close()
    return rows
