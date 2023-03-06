import pandas as pd
import os
import dotenv
import maskpass
from sqlalchemy import sql, create_engine


class Database:
    def __init__(self, conn_string):
        self.conn_string = conn_string

    def make_connection(self):
        """Creates an engine object using a database connect string. Uses the connect() method on the engine object to
            create an engine.connect object (connection to the database)

            :return: engine.connect object - connection to the database
            """

        engine = create_engine(f"postgresql://{self.conn_string}")

        conn = engine.connect()

        return conn


def select(conn, q):
    """
    Sends a query to the database and returns a Dataframe object

    :param conn: engine.connect object - same object returned from make_connection()
    :param q: string - sql query from user input
    :return: Dataframe - Dataframe created from read_sql_query function from the pandas module
    """
    rows = pd.read_sql_query(sql.text(q), conn)
    conn.close()
    return rows


def query(conn, q):
    """
    Executes an update, insert, or delete statement in a database

    :param conn: engine.connect object - same object returned from make_connection()
    :param q: string - sql query from user input
    """
    conn.execute(q)
    conn.close()


def use_default():
    """
    Takes in database information from secrets.env and turns it into a connection string

    :return: string - a formatted connection string to a database to be used in query().
    """
    dotenv.load_dotenv("secrets.env")
    host = os.getenv("DBHOST")
    name = os.getenv("DBNAME")
    user = os.getenv("DBUSER")
    password = os.getenv("DBPASS")
    port = os.getenv("DBPORT")

    return f"{user}:{password}@{host}:{port}/{name}"


def use_own():
    """
    Takes in database information from user input and turns it into a connection string

    :return: string - a formatted connection string to a database to be used in query().
    """
    host = input("What is the host for your database? Example: localhost ")
    name = input("What is the name of your database? ")
    user = input("What is the username for your database? ")
    password = maskpass.askpass("What is the password for your database? ")
    port = input("What is the port for your database? ")

    return f"{user}:{password}@{host}:{port}/{name}"
