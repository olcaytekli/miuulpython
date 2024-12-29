# """
# 1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın.
# ** "random modülü" için "python random" şeklinde arama yapın.
# ** 100 üzerinden puanlama yapın. Her soru 20 puan.
# ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.

# """
# import random

# hak = int(input("Oyuna hoş geldiniz, kaç hak istiyorsunuz? "))
# print(f"Toplam tahmin hakkınız: {hak}")

# rastgele_sayi = random.randint(1,50)
# print(rastgele_sayi)
# sayac = 0
# puan = 100
# while hak > 0:
#     hak -=1
#     sayac += 1
#     tahmin = int(input("Tahmininizi girin: "))

#     if rastgele_sayi == tahmin:
#         kalan = puan - ((100 / hak) * (sayac - 1))   
#         print(f"Tebrikler {sayac}. hakkınızda bildiniz.Toplam puanınız:{kalan}")
#         break
#     elif rastgele_sayi > tahmin:
#         print("Daha büyük bir sayı söyleyin.")
#     elif rastgele_sayi < tahmin:
#         print("Daha küçük bir sayı söyleyin.")

#     if hak == 0:
#         print(f"Hakkınız bitti. Tutulan sayı {rastgele_sayi}")



############# ASAL SAYI ###################
"""
Soru : Girlilen bir sayının asal olup olmadığını bulun.

"""
sayi = int(input("Bir sayı girin: "))
asalmi = True

if sayi == 1:
    asalmi = False

for i in range(2, sayi):
    if sayi % i == 0:
        asalmi = False
        break
if asalmi:
    print("Sayı asaldır")
else:
    print("sayı asal değildir.")







