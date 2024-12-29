# 1-100 e kadar

# x = 1
# while x<=100:
#     if x % 2 == 1:
#         print(f"sayı tek: {x}")
#     else:
#         print(f"sayı çift: {x}")
#     x += 1
# print("bitti...")


# name = ""       #false

# while not name.strip():
#     name = input("İsminizi girin: ")
# print(f"Merhaba {name}")


#############Uygulama############

# sayilar = [1,3,5,7,9,12,19,21]

# 1- sayilar listesini while ekrana yazdırın.
# i = 0
# while (i < len(sayilar)): 
#     print(sayilar[i])
#     i += 1

# 2 - Başlangıç ve bitiş değerlerini kullanıcdan alıp aradaki tüm tek sayıları
# ekrana yazdırın.

# baş = int(input("Başlangıç sayısını girin: "))
# son = int(input("Bitiş sayısını girin: "))

# i = baş
# while i < son :
#     i += 1
#     if i % 2 == 1:
#         print(i)
   


# 3 - 1-100 arasındaki sayıları azalan şekilde yazdırın.

# x = 100

# while 0 < x <= 100:
#     x -= 1
#     print(x)


# 4 - Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
# numbers = [] 

# i = 0

# while i < 5:
#      sayi = int(input('sayi :'))
#      numbers.append(sayi)
#      i+=1
# numbers.sort()    #sıralama için gerekli
# print(numbers)





# 5 - Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde
# saklayınız.
# **Urun sayısını kullancıya sorun.
# **Dictionary listesi yapısı(name,price) şeklinde olsun.
# **Urun ekleme işlemi bittiğinde ürünleri ekranda while ile listeyelin.

urunler = []
sayı = int(input("Ürün sayısı: "))

i = 0

while i < sayı:
    urun_adı = input("ad: ")
    fiyat = float(input("Fiyat: "))
    urunler.append({
         
         "name": urun_adı  ,
         "price": fiyat

    })
    i += 1

for urun in urunler:
         print(f'ürün adı: {urun['name']} ve ürün fiyatı {urun['price']}')
