# The Python Database API

import pymysql

db=pymysql.connect("localhost","root","123456","world")
cursor=db.cursor()
cursor.execute("SELECT VERSION()")

db.close()