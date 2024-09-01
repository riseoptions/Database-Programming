# 6- Insert Example

# Use your utility module.
import myconnutils
import pymysql.cursors  

connection = myconnutils.getConnection() 
print ("Connect successful!")  

try :
    cursor = connection.cursor() 
    sql = "Select max(Population) as Max_Grade from country "
    cursor.execute(sql) 
    # 1 row.
    oneRow = cursor.fetchone()      

    # Output: {'Max_Grade': 4} or {'Max_Grade': None}
    print ("Row Result: ", oneRow) 
    grade = 701
    
    if oneRow != None and oneRow["Max_Grade"] != None:
        grade = oneRow["Max_Grade"] + 701 
    cursor = connection.cursor()  
    sql =  "Insert into staff (id, first_name, last_name) " \
         + " values (%s, %s, %s) " 
    print ("Insert Grade: ", grade)
    
    # Execute sql, and pass 3 parameters.
    cursor.execute(sql, (grade, 'Zi', 'Zu' ) ) 
    connection.commit()  

finally: 
    connection.close()