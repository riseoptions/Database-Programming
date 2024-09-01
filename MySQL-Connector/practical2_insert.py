# Practical 2, 

import mysql.connector

#Connection to MySQL Server and database student
con = mysql.connector.connect(host="localhost", user="root", passwd="123456",\
database="student")
mycursor = con.cursor()

#Creating result Table
mycursor.execute("DROP TABLE IF EXISTS result")
mycursor.execute("CREATE TABLE result (name VARCHAR(30),\
phys INT(3), chem INT(3), math INT(3))")

#Inserting Rows in to the table
sql = """INSERT INTO result(name, phys, chem, math)
VALUES(%s, %s, %s, %s)"""
rows = [('Amit', 70,76,80),('Sudha',80,85,90),('Suma',50,70,90),\
('Paresh',55,60,70),('Ali',80,70,75),('Gargi',80,60,80)]
mycursor.executemany(sql, rows)
con.commit()

# Increasing marks of math by 5 for Sudha
sql = "UPDATE result SET math=math+5 WHERE name='%s'" % ('Sudha')
mycursor.execute(sql)

#To fetch the records and display
sql = "SELECT * FROM result"
mycursor.execute(sql)
result = mycursor.fetchall()
for row in result:
    name = row[0]
    p = row[1]
    c = row[2]
    m = row[3]
    print("Name=%s, Phys=%d, Chem=%d, Math=%d" % (name,p,c,m))

con.close()