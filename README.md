# CLI Database Query Tool

This is a CLI tool I created that can query a database either locally or remotely. You will need to create a secrets.env with the following variables:

DBNAME
DBUSER
DBPASS
DBPORT

Upon execution of the program it will ask you to enter a SQL query, if invalid the program will error out and end. Upon entering your SQL query, as long
as the DB connection and query are valid, the tool will stdout the data you requested. It then will ask if you would like to save as a csv file.
Either type Y for yes or N for no, for now the file will save as a test.csv in your downloads directory.

Now the program will ask if you will like to make another query, either type Y for yes and N for no. If yes the process will begin again, if no the program
will break out and end the process.
