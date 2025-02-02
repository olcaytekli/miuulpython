# 1-Workbench IDE ile schooldb isminde bir database oluşturup Student tablosunu ekleyiniz.
# Id, StudentNumber,Name,Surname,Birthdate,Gender


# 2-Database bağlantısını oluşturunuz.

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="mysql123",
    database ="schooldb"

)

print(mydb)