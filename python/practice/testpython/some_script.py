import mysql.connector

mydb = mysql.connector.connect(
    host="LeAnh",
    user="LeAnh",
    passwd="Hoimanchi2@",
    database= "mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")


