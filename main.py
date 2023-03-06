import db

while True:

    db_selection = input("Would you like to use the default database or use your own? ")
    if db_selection.lower() != "default":
        conn_string = db.use_own()
    else:
        conn_string = db.use_default()

    database = db.Database(conn_string)
    conn = database.make_connection()
    query = input("Please enter a SQL query: ")

    if "select" in query.lower():
        rows = db.select(conn, query)
        print(rows)

        result = input("Would you like to save as a csv file? Y/N: ")

        if result.lower() == "y":
            csv_name = input("What would you like the file name to be? ")
            csv_name += ".csv"

            rows.to_csv(rf'~/Downloads/{csv_name}', index=False)

            print("Your csv file will be in your downloads directory.")
    else:
        db.query(conn, query)
    cont = input("Would you like to run another query? Y/N: ")
    if cont.lower() == "y":
        continue

    print("Thank you for your query, please restart me to make another one!")
    break
