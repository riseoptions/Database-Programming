# 4- Connect MySQL from Python with PyMySQL
# https://o7planning.org/11463/connect-to-mysql-database-in-python-using-pymysql

import pymysql.cursors

# Connect to the database.
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',                             
                             db='world',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor) 
print ("connect successful!!")

try:  
    with connection.cursor() as cursor: 
        # SQL 
        sql = "SELECT Name, Population FROM country "
        
        # Execute query.
        cursor.execute(sql) 
        print ("cursor.description: ", cursor.description) 
        print()
        
        for row in cursor:
            print(row) 

finally:
    # Close connection.
    connection.close()