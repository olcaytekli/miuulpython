names = ["Ali","Yağmur","Hakan","Deniz"]
years = [1998,2000,1998,1987]

# 1.Soru "Cenk" ismini listenin sonuna ekleyiniz.

names.append("Cenk")
print(names)

# 2.Soru "Sena" değerini listenin başına ekleyiniz.

# names.insert(0,"Sena")
# print(names)

# 3.Soru "Deniz" ismini listeden siliniz.

# names.remove("Deniz")
# print(names)

# 4.Soru "Deniz" isminin indexi nedir?

# index = names.index("Deniz")
# names.pop(3)        3.indekstekini siler.

print(names)

# 5.Soru "Ali" listenin bir elemanı mıdır?

result = "Ali" in names
print(result)

# 6.Soru Liste elemanlarını ters çevirin.

# names.reverse()
# years.reverse()

# print(names)
# print(years)

# 7.Soru Liste elemanlarını alfabetik olarak sıralayınız.

# names.sort()
# years.sort()

# print(names)
# print(years)

# 8.Soru str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet, Dacia"
message = str.split(" ")
print(message)

# 9.Soru years dizisinin en büyük ve en küçük elemanı nedir?

value = max(years)
value1 = min(years)

print(value)
print(value1)

# 10.Soru years dizisinde kaç tane 1998 değeri verdır?

tane = years.count(1998)
print(tane)

# 11.Soru years dizisinin tüm elemanlarını silin.

# years.clear()
# print(years)

# 12.Soru Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

markalar = []

marka = input("Marka: ")
markalar.append(marka)

marka = input("Marka: ")
markalar.append(marka)

marka = input("Marka: ")
markalar.append(marka)

print(markalar)

