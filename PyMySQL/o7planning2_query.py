# 5- Query Example

# Use your utility module.
import myconnutils 

connection = myconnutils.getConnection() 
print ("Connect successful!")

sql = "Select Code, Name, Population from country Where Region = %s " 

try :
    cursor = connection.cursor() 
    # Execute sql, and pass 1 parameter.
    cursor.execute(sql, ( 'Polynesia' ) )  
    print ("cursor.description: ", cursor.description) 
    print()
    
    for row in cursor:
        print (" ----------- ")
        print("Row: ", row)
        print ("Code: ", row["Code"])
        print ("Name: ", row["Name"])
        print ("Population: ", row["Population"] , type(row["Population"]) ) 

finally:
    # Close connection.
    connection.close()