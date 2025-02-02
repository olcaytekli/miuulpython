import mysql.connector 

mydb = mysql.connector.connect(
    host = "localhost",  
    user = "root",
    password = "mysql123",
    database = "database"
)

mycursor = mydb.cursor()  
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), adress VARCHAR(255))") #DATABASE tablo oluşturmak için script
# mycursor.execute("SHOW DATABASES") #databaseleri göstermek için
# #mycursor.execute("CREATE DATABASE mydatabase")#yeni bir database oluşturmak istersek

# for x in mycursor:
#     print(x)

print(mydb)