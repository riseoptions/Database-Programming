# Practical

import mysql.connector

#Connection to MySQL Server
con = mysql.connector.connect(host="localhost", user="root", passwd="123456")
mycursor = con.cursor()

#Creating Student Database
mycursor.execute("DROP DATABASE IF EXISTS student")
mycursor.execute("CREATE DATABASE student")
mycursor.execute("USE student")

#Creating Studentinfo Table
mycursor.execute("DROP TABLE IF EXISTS studentinfo")
mycursor.execute("CREATE TABLE studentinfo (name VARCHAR(30), age INT(3), gender CHAR(1))")

#Inserting Rows in to the table
sql = """INSERT INTO studentinfo(name, age, gender)
VALUES(%s, %s, %s)"""
rows = [('Amit', 18,'M'),('Sudha',17,'F'),('Suma',19,'F'),\
        ('Paresh',19,'M'),('Ali',17,'M'),('Gargi',17,'F')]
mycursor.executemany(sql, rows)
con.commit()

#To fetch the records and display
sql = "SELECT * FROM studentinfo"
mycursor.execute(sql)
result = mycursor.fetchall()
for row in result:
    name = row[0]
    age = row[1]
    gender = row[2]
    print("Name=%s, Age=%d, Gender=%c" % (name,age,gender))

con.close()
