# This is a Python script that connects to a MySQL database using the mysql-connector-python library.
# It creates a connection to the database and initializes a cursor object for executing SQL queries.
# It also includes a comment indicating that the script is part of a Django project, specifically for managing a complaint management system.
# Importing the mysql.connector module to connect to MySQL database
# download mysql
# pip install mysql
# pip install mysql-connector-python
import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    
)

# Creating a cursor object using the cursor() method
cursorObject = dataBase.cursor()

# Creating a database named "rocdb"
cursorObject.execute("CREATE DATABASE rocdb")

print("Database created successfully!")
# Closing the cursor and connection