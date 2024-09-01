# https://o7planning.org/11463/connect-to-mysql-database-in-python-using-pymysql

import pymysql.cursors   
# Function return a connection.
def getConnection(): 
    # You can change the connection arguments.
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='123456',                             
                                 db='world',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection