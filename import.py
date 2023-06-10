import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mercur1453H*",
    database="testdatabase"
    )

mycursor = db.cursor()

