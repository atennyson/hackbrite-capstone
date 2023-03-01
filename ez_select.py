import db
import os
import dotenv
import maskpass

while True:

    db_selection = input("Would you like to use the default database or use your own?")
    if db_selection.lower() != "default":
        db.host = input("What is the host for your database? Example: localhost ")
        db.name = input("What is the name of your database? ")
        db.user = input("What is the username for your database? ")
        db.password = maskpass.askpass("What is the password for your database? ")
        db.port = input("What is the port for your database? ")
    else:
        dotenv.load_dotenv("secrets.env")
        db.host = os.getenv("DBHOST")
        db.name = os.getenv("DBNAME")
        db.user = os.getenv("DBUSER")
        db.password = os.getenv("DBPASS")
        db.port = os.getenv("DBPORT")

    con = db.make_connection()
    query = input("Please enter a SQL SELECT query: ")

    rows = db.db_query(con, query)

    print(rows)

    result = input("Would you like to save as a csv file? Y/N: ")

    if result.lower() == "y":
        csv_name = input("What would you like the file name to be? ")
        csv_name += ".csv"

        rows.to_csv(rf'~/Downloads/{csv_name}', index=False)

        print("Your csv file will be in your downloads directory.")

    cont = input("Would you like to run another query? Y/N: ")
    if cont.lower() == "y":
        continue

    print("Thank you for your query, please restart me to make another one!")
    break

