# Practical 4

import mysql.connector

#Connection to MySQL Server and database student
con = mysql.connector.connect(host="localhost", user="root", passwd="123456",\
database="student")
mycursor = con.cursor()

#Creating result Table
mycursor.execute("DROP TABLE IF EXISTS staff")
mycursor.execute("CREATE TABLE staff (name VARCHAR(30),\
desg VARCHAR(10), subject VARCHAR(10), salary INT(5))")

# Inserting six rows in staff
sql = """INSERT INTO staff(name, desg, subject, salary)
VALUES(%s, %s, %s, %s)"""
rows = [('Amit', 'PGT','CHEM',8000),('Sudha','HDM','BIOL',8500),\
('Suma','TGT','MATH',9000),('Paresh','PGT','HIND',7000),\
('Ali','PRT','COMM',7500),('Gargi','PGT','COMP',9000)]
mycursor.executemany(sql, rows)
con.commit()

#To fetch the records and display
sql = "SELECT * FROM staff WHERE salary>'%d'" % (8000)
mycursor.execute(sql)
result = mycursor.fetchall()
for row in result:
    name = row[0]
    des = row[1]
    sub = row[2]
    sal = row[3]
    print("Name=%s, Desg=%s, Subject=%s, Salary=%d" % (name,des,sub,sal))
    
con.close()