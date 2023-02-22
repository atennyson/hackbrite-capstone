import db
import pandas as pd

while True:

    con = db.make_connection(db.name, db.user, db.password, db.port)
    query = input("Please submit a SQL query: ")

    rows = db.db_query(con, query)

    df = pd.DataFrame(rows)
    print(df)

    result = input("Would you like to save as a csv file? Y/N: ")

    if result.lower() == "y":
        file_name = input("What would you like the file name to be? ")
        df.to_csv(rf'~/Downloads/{file_name}', index=False)

    cont = input("Would you like to run another query? Y/N: ")
    if cont.lower() == "y":
        continue

    print("Thank you for your query, please restart me to make another one!")
    break

