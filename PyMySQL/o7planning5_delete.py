# 8- Delete Example

# Use your utility module.
import myconnutils 

connection = myconnutils.getConnection() 
print ("Connect successful!")

try :
    cursor = connection.cursor() 
    sql = "Delete from staff where id = %s"  
    
    # Execute sql, and pass 1 parameters.
    rowCount = cursor.execute(sql, ( 702 ) ) 
    connection.commit()  
    print ("Deleted! ", rowCount, " rows") 

finally:
    # Close connection.
    connection.close()