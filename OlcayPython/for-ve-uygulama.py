# numbers = [1,2,3,4,5]

# for num in numbers:    #listenin içerisinden tek tek elemanları al ve num içerisine at ve her for döngüsünde num ı yazdır.
#     print(num)         #printin içine hello yazarsak bize 5 defa hello verir. Bunun nedeni liste elemanının sayısı kadar çıktı vermesi.


# names = ["çınar","sadık","sena"]

# for name in names:
#     print(f"my name is {name}")


# name = "Olcay tekli"  #stringler bir karakter dizisdiir bundan dolayı cevapta bize tek tek o l c vs diye verir.

# for n in name:
#     print(n)

# tuple = [(1,2),(3,4),(5,7)]
# for a,b in tuple:
#     print(a,b)

# d = {"k1":1 ,"k2":2, "k3":3}
# for item in d:      #sadece key bilgilerini aldı yani k1,k2,k3
#     print(item)

# d = {"k1":1 ,"k2":2, "k3":3}
# for key,value in d.items():      #sadece key ve valueları aldı
#     print(key,value)


#######Uygulama######

# sayilar = [1,3,5,7,9,12,19,21]

# 1-Sayılar listesinde hangi sayılar 3'ün katıdır?

# for sayı in sayilar:
#     if sayı % 3 == 0:
#         print (f"{sayı} :3'ün katıdır.")
#     else:
#         print(f"{sayı} :3'ün katı değildir.")
    


# 2-Sayılar listesinde sayıların toplamı kaçtır?
# sayilar = [1,3,5,7,9,12,19,21]
# toplam = 0

# for sayı in sayilar:
#     toplam = toplam + sayı
# print("toplam:" , toplam)

# 3-Sayılar listesindeki tek sayıların karesini alınız.

# for sayı in sayilar:
#     if sayı % 2 == 1:
#         toplam = sayı ** 2 
#         print(toplam)

# sehirler = ["kocaeli","istanbul","ankara","izmir","rize"]

# 4- Şehirlerden hangileri en fazla 5 karakterlidir ?

# for sehir in sehirler:
#     if len(sehir) <= 5:
#         print(sehir)

    

# 5-Ürünlerin fiyatları toplamı nedir?

# urunler = [
#     {"name": "samgung S6", "price": "3000"},
#     {"name": "samgung S7", "price": "4000"},
#     {"name": "samgung S8", "price": "5000"},
#     {"name": "samgung S9", "price": "6000"},
#     {"name": "samgung S10", "price": "7000"}
# ]
# # toplam = 0

# # for urun in urunler:
# #     toplam += int(urun["price"])
# # print(toplam)

# # 6-Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz?

# for urun in urunler:
#     if int(urun["price"]) <= 5000 : 
#         print(urun["name"])