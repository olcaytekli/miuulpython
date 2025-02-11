import mysql.connector
from datetime import datetime
from Student1 import Student
from Teacher1 import Teacher

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="mysql123",
    database ="schooldb"
)

class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getStudentById(self,id):   
        sql = "select * from studeny where id = %s"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("error", err)
    def deleteStudent(self,studentid):
        sql = "delete from student where id = %s"
        values = (studentid,)
        self.cursor.execute(sql,values)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print("Hata:", err)
        finally:
            self.connection.close()
    
    def getClasses(self):
        sql = "select * from class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print("error", err)

    def getStudentByClassId(self,classid):  
        sql = "select * from student where classid = %s"
        value = (classid,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("error", err)
     
    def addStudent(self,student:Student):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender,ClassId) VALUES(%s,%s,%s,%s,%s,%s)"
        values = (student.studentNumber,student.name,student.surname,student.birthdate,student.gender,student.classid)
        self.cursor.execute(sql,values)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print("Hata:", err)
        finally:
            self.connection.close()
    def addorEditStudent(self,student:Student):
        pass

    def editStudent(self,student: Student):
        sql ="update student set studentnumber =%s,name=%s,surname=%s,birthdate=%s,gender=%s,classid = %s where id =%s"
        values = (student.studentNumber,student.name,student.surname,student.birthdate,student.gender,student.classid,student.id)
        self.cursor.execute(sql,values)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt güncellendi.")
        except mysql.connector.Error as err:
            print("Hata:", err)
        finally:
            self.connection.close()

    def addTeacher(self,teacher : Teacher):
        pass

    def editTeacher(self,teacher:Teacher):
        pass

    def __del__(self):
        self.connection.close()
        print("db silindi")




db = DbManager() 

student = db.getStudentById(7)
student[0].name = "Çınar"
student[0].surname = "Turan"
student[0].studentNumber = "501"

# db.addStudent(student[0])
db.editStudent(student[0])



# print(student[0].name)
# print(student[0].surname)

# student = db.getStudentByClassId(1)
# print(student[0].name)