import sqlite3


connection = sqlite3.connect("db/testdb.db")
cursor = connection.cursor()

# create table
query = '''CREATE TABLE IF NOT EXISTS Person 
        (PID INTEGER PRIMARY  KEY AUTOINCREMENT,
         NAME  VARCHAR(100),
         HEIGHT INT)'''
cursor.execute(query)

# insert data to table

insert = "INSERT INTO Person (NAME, HEIGHT) VALUES ('LE VAN ANH', 163)"
cursor.execute(insert)

