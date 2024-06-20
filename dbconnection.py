import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="deevennancy1@",
    database = "customerdata"
)

mycur = conn.cursor()

if(mycur):
    print("Successs")
else:
    print("Failed")

query = "create table studentdb(name varchar(10),rollno varchar(100));"
mycur.execute(query)