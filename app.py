import db
import pandas as pd


query = input("Please submit a SQL query: ")

rows = db.db_query(db.con, query)

df = pd.DataFrame(rows)
print(df)

result = input("Would you like to save as a csv file? Y/N: ")

if result.lower() == "y":
    df.to_csv(r'~/Downloads/test.csv', index=False)

print("Thank you for your query, please restart me to make another one!")

