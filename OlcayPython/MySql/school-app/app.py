from dbmanager import DbManager
from Student1 import Student
import datetime 

class App:
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        msg = "****\n1-Öğrenci Listesi\n2-Öğreci Ekle\n3Öğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-Sınıflara Göre Dersler\n7-Çıkış(E/Ç)"
        while True:
            print(msg)
            islem = input("Seçim: ")
            if islem == "1":
                self.displayStudents()
            elif islem == "2":
                self.addStudent()
            elif islem =="3":
                self.editStudent()
            elif islem == "4":
                self.deleteStudent()
            elif islem == "E" or islem == "Ç":
                break
            else:
                print("yanlış seçim")

    def deleteStudent(self):
        classid = self.displayStudents()
        studentid = int(input("öğrenci id: "))

        self.db.deleteStudent(studentid)
    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input("öğrenci id: "))

        student = self.db.getStudentById(studentid)

        studentid[0].name = input("name:") or student[0].name
        studentid[0].surname = input("surname:") or student[0].surname
        studentid[0].gender = input("cinsiyet (E/K):") or student[0].gender
        studentid[0].classid = input("sınıf: ") or student[0].classid

        year = input("yıl: ") or student[0].birthdate.year
        month = input("ay: ") or student[0].birthdate.month
        day = input("gün: ") or student[0].birthdate.day

        Student[0].birthdate = datetime.date(year,month,day)
        self.db.editStudent(student[0])

    def addStudent(self):
        self.displayClasses()
        classid = int(input("Hangi sınıf: "))
        number = input("Numara: ")
        name = input("Ad:")
        surname = input("Soyad:")
        year = int(input("yıl"))
        month = int(input("ay:"))
        day = int(input("gün:"))
        gender = input("cinsiyet (E/K)")
        birthdate = datetime.date(year,month,day)

        student = Student(None,number,name,surname,birthdate,gender,classid)
        self.db.addStudent(student)

    def displayClasses(self):
        classes = self.db.getClasses()
        for c in classes:
            print(f"{c.id}: {c.name}")


    def displayStudents(self):
        self.displayClasses()
        classid = int(input("Hangi sınıf: "))

        students = self.db.getStudentByClassId(classid)
        print("Öğrenci listesi")
        for std in students:
            print(f"{std.id} - {std.name} {std.surname}")

        return classid

app = App()
app.initApp


