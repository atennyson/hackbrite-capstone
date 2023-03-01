import pandas as pd
import os
import dotenv
import maskpass
from sqlalchemy import create_engine


def make_connection(host, name, user, password, port):
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


def use_default():
    dotenv.load_dotenv("secrets.env")
    host = os.getenv("DBHOST")
    name = os.getenv("DBNAME")
    user = os.getenv("DBUSER")
    password = os.getenv("DBPASS")
    port = os.getenv("DBPORT")

    return host, name, user, password, port


def use_own():
    host = input("What is the host for your database? Example: localhost ")
    name = input("What is the name of your database? ")
    user = input("What is the username for your database? ")
    password = maskpass.askpass("What is the password for your database? ")
    port = input("What is the port for your database? ")

    return host, name, user, password, port
