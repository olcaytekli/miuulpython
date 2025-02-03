# 1-Workbench IDE ile schooldb isminde bir database oluşturup Student tablosunu ekleyiniz.
# Id, StudentNumber,Name,Surname,Birthdate,Gender

# 2-Database bağlantısını oluşturunuz.

#3- Aşağıdaki bilgiler için insert sorguları oluşturup kayıtları ekleyiniz.
# ("101", "Ahmet", "Yılmaz", datetie.datetie(2005, 5, 17), "E"),
# ("102", "Ali", "Can", datetie.datetie(2005, 6, 17), "E"),
# ("103", "Canan", "Tan", datetie.datetie(2005, 7, 7), "K"),
# ("104", "Ayşe", "Taner", datetie.datetie(2005, 9, 23), "K"),
# ("105", "Bahadır", "Toksöz", datetie.datetim(2004, 7, 27), "E"),
# ("106", "Ali", "Cenk", datetie.datetie(2003, 8, 25), "E")


import mysql.connector
from datetime import datetime
from sqlconnection import connection

class Student:
    connection = connection 
    mycursor = connection.cursor()

    def __init__(self,studentNumber,name,surname,birthdate,gender):
        self.studentNumber = studentNumber
        self.name = name 
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def saveStudent(self):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"
        values = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender)
        Student.mycursor.execute(sql,values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print("Hata:", err)
        finally:
            Student.connection.close()

ahmet = Student("202","ahmet","yılmaz",datetime(2005, 5, 17),"E")
ahmet.saveStudent()


# ogrenciler=[
#     ("101", "Ahmet", "Yılmaz", datetime(2005, 5, 17), "E"),
#     ("102", "Ali", "Can", datetime(2005, 6, 17), "E"),
#     ("103", "Canan", "Tan", datetime(2005, 7, 7), "K"),
#     ("104", "Ayşe", "Taner", datetime(2005, 9, 23), "K"),
#     ("105", "Bahadır", "Toksöz", datetime(2004, 7, 27), "E"),
#     ("106", "Ali", "Cenk", datetime(2003, 8, 25), "E")
# ]

# mycursor.executemany(sql, ogrenciler)

# try:
#     connection.commit()
#     print(f"{mycursor.rowcount} tane kayıt eklendi.")
# except mysql.connector.Error as err:
#     print("Hata:", err)
# finally:
#     connection.close()
