# name = "Olcay"
# surname = "Tekli"
# age = 24 

# greeting = "My name is " +  name + " " +  surname + " and I am "+ str(age) + " years old"
#bu greetingi print'in içine yazarsak yine aynı cevabı verir

#print ("My name is " +  name + " " +  surname + " and I am "+ str(age) + " years old. ")

# Bir cümlenin başına \n yazarsak onu alt satıra yazar. 

#print(greeting)

# print(greeting[0])  #bu bize greeting girdisinin ilk basamağında ne varsa onu verir.
# print(greeting[3])   

#peki son basamağındakini istersek?

#print (len(greeting))  bu greetingin kaç basamaktan oluştuğunu söyler
#length = len(greeting)
# print (greeting[length-1]) #son basamak -1
#print(greeting[3:7])    3'ten 7'ye kadar string bilgisini verir
#print (greeting[3:])    3'ten başlar sonuna kadar gider
#print (greeting[:15])   Baştan başlar 15'e kadar gider.
#print (greeting[2:40:2])   2'den başlar 40'a kadar iki adımda bir alır.

#FORMAT METODU

name = "Çınar"
surname = "Turan"
age = 24
#print ("My name is {} {}" .format(name, surname))
#print ("My name is {0} {1}" .format(name, surname))  index numaraları ile de yazabiliriz.
#print ("My name is {n} {s}" .format(n=name, s=surname))  değişkenlerle de yapılabilir
# print ("My name is {} {} and I am {} years old." .format (name, surname, "24"))  #age bilgisi de tanımlayabiliriz.

# result = 200 / 700
# print ("the result is {r:1.3}" .format(r=result)) #1 alanlık boşluk bırak ve virgülden sonra 3 basamaklı yaz demek


# print (f"My name is {name} {surname} and I am {age} years old.") 
