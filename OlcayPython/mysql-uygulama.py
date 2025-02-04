# Aşağıdaki sorguları yazınız:

# a. Tüm öğrenci kayıtlarını alınız.
# b. Tüm öğrencilerin sadece öğrenci no, ad ve soyad bilgilerini alınız.
# c. Sadece kız öğrencilerin ad ve soyadlarını alınız.
# d. 2003 doğumlu öğrenci bilgilerini alınız.
# e. İsmi Ali ve doğum tarihi 2005 olan öğrenci bilgilerini alınız.
# f. Ad veya soyadı içinde 'an' ifadesi geçen kayıtları alınız.
# g. Kaç erkek öğrenci vardır?
# h. Kız öğrencileri harf sırasına göre getiriniz.

import mysql.connector
from datetime import datetime
from sqlconnection import connection

class Student:
    connection = connection 
    mycursor = connection.cursor()

    def __init__(self,id,studentNumber,name,surname,birthdate,gender):
        if id is None:
            self.id = 0
        else:
            self.id = id
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

    @staticmethod
    def saveStudents(students):

        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)"
        values = students
        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print("hata:", err)
        finally:
            Student.connection.close()

    @staticmethod
    def StudentInfo():
        sql = "Select * from student LIMIT 5"  #İLK 5 kayıt gelsin istersek
        # sql = "Select studentnumber,name,surname from student"
        # sql = "Select name,surname from student where gender ='K'"
        # sql = "Select * from student where YEAR(birthdate) = 2003"  #birthdate içinden yıl bilgisini getiriyor MONTH da yazabiliriz
        # sql = "Select * from student where YEAR(birthdate) = 2005 and name = 'Ali' "  
        # sql = "Select * from student where name like '%an%' or surname like '%an%'"  
        # sql = "Select COUNT(*) from student where gender='E' "  
        # sql = "Select COUNT(id) from student where gender='E' "  
        # sql = "Select name,surname from student where gender='K' order by name,surname"  

        Student.mycursor.execute(sql)

        try: 
            results = Student.mycursor.fetchall()
            print(results)

            for result in results:
                print(f"{results} ")  #bu bölüm istediğimin bilgiye göre değişkenlik gösterir
        except mysql.connector.Error as err:
            print("hata",err)
        # finally:
        #     Student.connection.close()
# Student.StudentInfo()

    @staticmethod
    def getStudentsGender(gender):
        sql = "select * from student where gender = %s"
        value = (gender,)
        
        Student.mycursor.execute(sql,value)

        try:
            return Student.mycursor.fetchall()
        except mysql.connector.Error as err:
            print("Error", err)

    @staticmethod
    def updateStudents(liste):
        sql ="update student set studentnumber =%s,name=%s,surname=%s,birthdate=%s,gender=%s where id =%s"
        values = []
        order = [1,2,3,4,5,0]
        for item in liste:
            item = [item[i] for i in order]
            values.append(item)
        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt güncellendi")
        except mysql.connector.Error as err:
            print("hata:", err)


# student = Student.getStudentById(8)

# student.name = "Çınar"
# student.surname ="Turan"

# student.updateStudent()

students = Student.getStudentsGender("E")
print(students)

liste = []
for std in students:
    std = list(std)
    std[2] = 'Mr '+ std[2]
    liste.append(std)
Student.updateStudents(liste)
    

