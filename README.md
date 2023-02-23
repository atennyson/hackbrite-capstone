# CLI Database Query Tool

### YOU WILL NEED YOUR OWN POSTGRES DATABASE TO USE THIS CLI TOOL

This is a CLI tool I created that can query a database either locally or remotely. You will need to create a secrets.env with the following variables:

DBHOST
DBNAME
DBUSER
DBPASS
DBPORT

Store your database info into these variables as we will use these to build the connection string in ```make_connection```

Upon execution of the program it will ask you to enter a SQL query, if invalid the program will error out and end (WIP). Upon entering your SQL query, as long
as the DB connection and query are valid, the tool will stdout the data you requested to the command line. It then will ask if you would like to save as a csv file.
Either type Y for yes or N for no.

If you choose to save the data, the program will then ask you to name the file. Once named, the file will be saved in your ~/Downloads directory.

Now the program will ask if you will like to make another query, either type Y for yes and N for no. If yes the process will begin again, if no the program
will break out and end the process.
