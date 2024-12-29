# 1.Soru "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir lise oluşturunuz.

list = ["Bmw", "Mercedes","Opel","Mazda"]

# # 2.Soru Liste Kaç Elemanlıdır?
# result = len(list)
# print(result)

# 3.Soru Listenin ilk ve son elemanı nedir?

print(list[0],list[3])

# 4.Soru Mazda değerini Toyota ile değiştirin.
list = ["Bmw", "Mercedes","Opel","Mazda"]
list[-1] = "Toyota"
print(list)

# 5.Soru Mercedes listenin bir elemanı mıdır?
list = ["Bmw", "Mercedes","Opel","Toyota"]

isFound = "Mercedes" in list
print (isFound)

# 6. Soru Listenin -2 indeksindeki değer nedir?

print(list[-2])

# 7.Soru Lisenin ilk 3 elemanını alın.

print(list[0:3])

# 8.Soru Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
list[-2:] = "Toyota" , "Renault"
print(list)

# 9.Soru Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.

result = list + ["Audi","Nissan"]
print(result)

# 10.Soru Listenin son elemanını silin.

del list[-1]
result1 = list
print(result1) 

# 11.Soru Liste elemanlarını tersten yazdırın.

result = list[::-1]
print(result)

# 12.Soru Aşağıdaki verileri bir liste içinde saklayınız.

# student A: Yiğit Bilgi 2010, (70,60,70)
# student B: Sena Turan 1999, (80,80,70)
# student C: Ahmet Turan 1988, (80,70,90)

studentA = ["Yiğit" , "Bilgi",2010,[70,60,70]]
studentB = ["Sena","Turan",1999, [80,80,70]]
studentC = ["Ahmet","Turan", 1998, [80,70,90]]

students = studentA[0]
students = studentB[1]
students = studentC[3]

students = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}"
print(students)








































