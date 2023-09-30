import mysql.connector 

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '111aaaAAA!' 
)

# prepare a cursor obj 
cursorObject = dataBase.cursor() 

# create a db 
cursorObject.execute("CREATE DATABASE crmdb") 

print("All Done!")