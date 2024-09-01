# Introduction to Database Programming in Python

import mysql.connector

# Connecting to the database server
con = mysql.connector.connect(host="localhost", user="root", passwd="123456")
mycursor = con.cursor()

# Creating a Database
mycursor.execute("DROP DATABASE IF EXISTS rise3")
mycursor.execute("CREATE DATABASE rise3")
mycursor.execute("USE rise3")

# Creating the Table
mycursor.execute("DROP TABLE IF EXISTS studentinfo")
mycursor.execute("CREATE TABLE studentinfo (name VARCHAR(30), age INT(3), gender CHAR(1))")

# Inserting data into the table
sql = """INSERT INTO studentinfo(name, age, gender)
VALUES('Ashok',17,'M')"""
mycursor.execute(sql)
con.commit()

# Inserting multiple rows simultaniously
sql = """INSERT INTO studentinfo(name, age, gender)
VALUES(%s, %s, %s)"""
rows = [('Amit', 18,'M'),('Sudha', 17, 'F')]
mycursor.executemany(sql, rows)
con.commit()


con.close()

