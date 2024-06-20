import mysql.connector
mydb = mysql.connector.connect(  host="localhost",  user="root",  password="deeven#123")
mycurs = mydb.cursor()
mycurs.execute("create database mydb")
mycurs.execute("SHOW DATABASES")

for db in mycurs:
    print(db)