'''
(f''fonk)
Kullanıcıdan alınan isim ve soyismi birleştirip, baş harflerini büyük harf yaparak ekrana yazdırın.
'''

# isim = input("İsminizi girin: ")
# soyad = input("Soyadınızı girin: ")
# isim1 = isim.title()
# isim2 = soyad.title()
# print(f"Adım {isim1} soyadım {isim2}")



'''
Bir sayının çift olup olmadığını kontrol eden kod dizini yazınız.
'''
# sayı = int(input("Bir sayı girin: "))

# if sayı % 2 == 0:
#     print(f"{sayı} sayısı bir çift sayıdır.")
# else:
#     print(f"{sayı} sayısı bir çift sayı değildir.")





# '''
# Girilen bir cümledeki kelime sayısını hesaplayın.
# '''
# cumle = []
# cumle = input("Bir cümle yazınız: ")
# cumle1 = cumle.split(" ")
# kelime_sayısı = len(cumle1)

# print(kelime_sayısı)


'''
(fordöngüsü)
sayilar = [12, 7, 9, 14, 18, 21, 4, 10]
Bir listedeki çift sayıları filtreleyip yeni bir liste oluşturun.
'''

# sayilar = [12, 7, 9, 14, 18, 21, 4, 10]
# tek_sayilar = []
# for tek in sayilar:
#     if tek % 2 == 1:
#         tek_sayilar.append(tek)
# print(tek_sayilar)





'''
(fordöngüsü)
Bir sayının faktöriyelini hesaplayın.
'''
# 3! = 3 . 2 . 1 = 6 

# sayi = int(input("Sayı girin: "))

# i = sayi
# faktoriyel = 1

# while i > 0:
#     faktoriyel *= i
#     i -= 1

# print(faktoriyel)

# sayi = int(input("Sayı girin: "))
# faktoriyel = 1

# for i in range(1, sayi + 1):
#  faktoriyel *= i
# print(faktoriyel)












'''
Kullanıcıdan alınan üç sayının toplamını ve ortalamasını hesaplayın.
'''
# a = int(input("1.Sayıyı girin: "))
# b = int(input("2.Sayıyı girin: "))
# c = int(input("3.Sayıyı girin: "))

# toplam = a + b + c
# ortalama = (a + b + c) / 3
# print(f"Bu sayıların toplamı : {toplam} , sayıların ortalaması: {ortalama}")

'''
Manavdaki elma,armut,muz ve çilek fiyatlarını sözlük 
özelliğini kullanarak rastgele fiyatlar vererek değerlerin toplamını hesaplayın.
'''





'''
sayilar = [45, 23, 67, 12, 89, 34, 56]
Bu listedeki en büyük ve en küçük eleman arasındaki farkı hesaplayın.
'''
# sayilar = [45, 23, 67, 12, 89, 34, 56]
# min_value = min(sayilar)
# max_value = max(sayilar)

# fark = max_value - min_value
# print(fark)




'''
(ifelse konusu)
Girilen sayının pozitif, negatif veya sıfır olduğunu kontrol eden program.
'''

# sayı = int(input("Bir sayı girin: "))

# if sayı > 0:
#     print("Sayı pozitiftir.")
# elif sayı < 0:
#     print("Sayı negatiftir.") 
# else:
#     print("Sayı sıfırdır.")



'''
(ifelse konusu)
Bir öğrencinin not ortalamasına göre geçme veya kalma durumunu belirleyen program
Ortalama 90 ve üzeri ise: "Pekiyi"
Ortalama 70-89 arası ise: "İyi"
Ortalama 50-69 arası ise: "Orta"
Ortalama 50'nin altı ise: "Kaldı"
'''

'''
(ifelse konusu)
Girilen saatteki çalışma durumuna göre mesaj veren program
Saat 9-17 arası: "Mesai saatleri içindesiniz."
Saat 17-22 arası: "Çalışma saatleri dışında, dinlenme zamanı."
Saat 22-9 arası: "Gece vakti, uyuma zamanı."

'''

""""
Soru: Basamakların Toplamı
Kullanıcıdan bir sayı alın ve bu sayının basamaklarının toplamını hesaplayın.
Örneğin:

Girdi: 538
Çıktı: 5 + 3 + 8 = 16
Kurallar:

Sayının negatif olup olmadığını kontrol edin. Eğer negatifse, pozitif yaparak devam edin.
Her bir basamağı ayrı ayrı bulun ve toplayın.
İşlem bittikten sonra sonucu kullanıcıya gösterin.
""" 
# # Kullanıcıdan sayı al
# sayi = int(input("Bir sayı girin: "))

# # Negatif sayılar için pozitif yap
# if sayi < 0:
#     sayi = abs(sayi)

# # Basamakların toplamını hesapla
# toplam = 0

# while sayi > 0:
#     toplam += sayi % 10  # Son basamağı ekle
#     sayi //= 10          # Son basamağı at

# print(f"Basamakların toplamı: {toplam}")

"""
Soru: Rakamların Çarpımını Hesaplama
Kullanıcıdan bir sayı al ve bu sayının rakamlarının çarpımını hesapla.

Örnek:

Girdi: 234
Çıktı: 2 * 3 * 4 = 24
Kurallar:

Sayının her basamağını tek tek al.
Basamakları çarparak sonucu bul.
Eğer kullanıcı 0 girerse, sonuç 0 olacak.


"""

# #525
# sayi = int(input("Bir sayı girin : "))

# if sayi < 0:
#     sayi = abs(sayi)

# carpim = 1

# while sayi > 0:
#     carpim *= sayi % 10
#     sayi = sayi // 10

# print(carpim)

