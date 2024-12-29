# # Object Oriented Programming (OOP)

#  #class
# class Person:   # bu metottan sonra bir kod gelmeli. If, for vs vs
#     #class attributes
#     address = "no info"    #her zaman kullanmayacaklarımızı class attr. içine
#     # constructor (yapıcı metod):
#     def __init__(self, name, year):          #self burada p1 ve p2 diğerleri ise bu p1 ve p2 içine aktaracağımız bilgiler
#     # init her obje için çalışıyor
    
#     #object attributes      
#         self.name = name     #constructor içine yollayacaklarımız 
#         self.year = year 

#     #instance methods
#     def intro (self):   #objelere hizmet edeceği için objenin referansı olan self yazdık
#         print("Hello there. I am " + self.name)

#     def calculateAge(self):
#         return 2019 - self.year
# # object (instance)
# p1 = Person(name = "ali",year = 1990)      #p1 objesi tanımlamış olduk
# p2 = Person(name = "yağmur",year= 1995)

# #updating
# p1.name = "ahmet"
# p1.address = "istanbul "
# p2.name = "oktay"

# #accessing object attributes
# print(f"p1: name: {p1.name} year:{p1.year} address: {p1.address}")
# print(f"p2 :name: {p2.name} year:{p2.year}") 

# p1.intro()       #intro metodunu p1 objesi üzerinden çağırıyoruz
# print(f"Yaşım : {p1.calculateAge()}")


##################################

class Circle:
    #Class object attribute

    pi = 3.14  # pi yi class ob. att. içine atma sebebimiz değişmeyen bir sabit olduğu için
    
    def __init__(self, yaricap=1):    #yaricap bilgisi verilmediği için 1 atadık
        self.yaricap = yaricap
    
    #Methods 
    def cevre_hesapla(self):
        return 2*self.pi * self.yaricap
    
    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)

c1 = Circle()    #yarıcap belirtmediğimiz için yarıçap =1
c2 = Circle(5)

print(f"C1 : alan = {c1.alan_hesapla()} çevre = {c1.cevre_hesapla()}")
print(f"C2 : alan = {c2.alan_hesapla()} çevre = {c2.cevre_hesapla( )}")

 