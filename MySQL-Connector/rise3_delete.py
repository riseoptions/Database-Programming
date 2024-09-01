# Introduction to Database Programming in Python

import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", passwd="123456")
mycursor = con.cursor()
mycursor.execute("USE rise3")

# Deleting Records from a Table
sql = "DELETE FROM studentinfo WHERE name='%s'" % ('Ashok')
mycursor.execute(sql)

sql = "SELECT * FROM studentinfo"
mycursor.execute(sql)
result = mycursor.fetchall()

for row in result:
    name = row[0]
    age = row[1]
    gender = row[2]
    print("Name=%s, Age=%d, Gender=%c" % (name,age,gender))
con.close()