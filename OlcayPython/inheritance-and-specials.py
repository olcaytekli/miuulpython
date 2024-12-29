# Inheritance (Kalıtım) : Miras alma

# Person => name, lastname, age, eat(), run(), drink()  
# Student(Person), Teacher(Person)   #yukarıdaki bilgileri diğer classlara da aktarmak istersek


#Animal => Dog(Animal), Cat(Animal)      #dog ve catin animal classının özelliklerini miras alması


class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        print("Person Created")
    
    def who_am_i(self):
        print("I am a person.")

    def eat(self):
        print("I am eating")

class Student(Person):
    def __init__(self,fname,lname,number):    #student içinde tekrardan fname lastname oluş. gerek yok bunu persondan alacağız
        Person.__init__(self,fname,lname)     #student oluşturulduğunda student ın init i personkini ezer fakat bunu yazdığımız için person initinden de gelir.
        self.studentNumber=number 
        print("Student Created")        #pass yer tutucudur yani şimdilik class için kod yazmamıza gerek yok.
    
    #override
    def who_am_i(self):   #aynı sınıflı bir metot temel seviyedekini ezer. Yani student who am i yazdırdığında person değil I am a student der
        print("I am a student")

    def sayHello(self):
        print("Hello I am a student.")

class Teacher(Person):
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname)
        self.branch = branch
    def who_am_i(self):
        print(f"I am a {self.branch} teacher ")



    


p1 = Person("Ali","Yılmaz")
s1 = Student("Çınar","Turan",1256)
t1 = Teacher("Oktay","Tekli","Fizik")
print(p1.firstname + " " + p1.lastname)
print(s1.firstname+ " "+ p1.lastname + " " + str(s1.studentNumber)) 

p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
s1.sayHello()
t1.who_am_i()



################ Specials ###################

myList = [1,2,3,4]

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie objesi oluşturuldu.")

    def __str__(self):
        return f"{self.title} by {self.director}"
    
    def __len__(self):
        return self.duration
    
    def __del__(self):
        print("film silindi")
m = Movie("film adı","yönetmen adı",120)

# print(str(myList))
print(str(m))
# print(len(myList))
# print(len(m))

