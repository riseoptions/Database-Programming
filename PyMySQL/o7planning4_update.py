# 7- Update Example 

# Use your utility module.
import myconnutils
import pymysql.cursors 
import datetime 

connection = myconnutils.getConnection() 
print ("Connect successful!")

try :
    cursor = connection.cursor() 
    sql = "Update staff set id = %s, first_name = %s where id = %s "   
    # Hire_Date
    newHireDate = datetime.date(2002, 10, 11) 
    # Execute sql, and pass 3 parameters.
    rowCount = cursor.execute(sql, (702, 'Yaz', 701 ) ) 
    connection.commit()  
    print ("Updated! ", rowCount, " rows")
    
finally:
    # Close connection.
    connection.close()