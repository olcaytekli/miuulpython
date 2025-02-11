website = "http://www.sadikturan.com"
course = "Pyhton Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

# 1.Soru "course" karakter dizisinde kaç karakter bulunmaktadır?

length = len(course)
print(length)

# 2.Soru  "website" içinden www karakterlerini alın.

#print(website[7:10])

# 3.Soru   "website" içinden com karakterlerini alın.

# print(website[22:25])    #baştan itibaren
# print(website[length-3:length])  #bu da diğer bir yol 

# # 4.Soru "course" içinden ilk 15 ve son 15 karakterlerini alın.

# print(course[:15])
# print(course[-15:])

# 5.Soru "course" ifadesindeki karakterleri tersten yazdırın.

print(course[::-1])

name, surname, age, job = "Bora" , "Yılmaz" , 32 , "mühendis"

#6.Soru Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#     "Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis."

#print("Benim adım " + name + " " + surname + " , " + "Yaşım " + str(age) + " ve " + "mesleğim " + job + ". " )
result = "Benim adım {} {}, Yaşım {} ve mesleğim {}. " .format(name,surname,age,job)
result = f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}"
print (result)  #süslü parantezlerin içine 0 dan başlayıp indexleri yazabiliriz hatta bunu yer değiştirmek için de yapabiliriz.

#7.Soru "Hello world" ifadesindeki w harfini "W" ile değiştirin.

s = "Hello world"
s = s[0:6] + "W" + s[-4:]
print(s)

# 8.Soru "abc" ifadesini yan yana 3 defa yazdırın.

harf = "abc "

print (harf * 3)