# # 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.

# def word(kelime,tekrar_sayisi):
#     for i in range(tekrar_sayisi):
#         print(kelime)

# word("Selam",4)

# # 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazın.

# def kelime(*params):
#     liste = []
#     for param in params:
#         liste.append(param)
#     return liste

# result = kelime(10,20,30,"Merhaba")
# print(result)





# 3-Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.


# def asalSayilariBul(sayi1 , sayi2):
#     for sayi in range(sayi1 , sayi2+1):
#         if sayi >1 :
#             for i in range(2,sayi):
#                 if (sayi % i ==0):
#                     break
#             else: 
#                 print(sayi)         

# sayi1 = int(input("sayı 1: "))
# sayi2 = int(input("sayi 2: "))  

# asalSayilariBul(sayi1, sayi2)







# 4-Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonk. yazın.

# def tam_bolen(sayi):
#     liste = []
#     for i in range(1,sayi+1):
#         if sayi % i == 0:
#             liste.append(i)

#     return liste

# result = tam_bolen(18)
# print(result)

# ogrenci_listesi = []

# def ogrenci_ekle(ogrenci_listesi):
#     isim = input("Öğrencinin adı: ")
#     ogrenci_listesi.append(isim)
#     print(f"Öğrenci {isim} listeye eklendi.")

# def ogrenci_sil(ogrenci_listesi):
#     isim = input("Silmek istediğiniz öğrenci: ")
#     if isim in ogrenci_listesi:
#         ogrenci_listesi.remove(isim)
#         print(f"Öğrenci {isim} listeden silindi. ")
#     else:
#         print(f"{isim}li öğrenci listede yok.")

# def liste(ogrenci_listesi):
#     if len(ogrenci_listesi) == 0:
#         print("Liste şu an boş.")
#     else:
#         print("Öğrenci listesi.")
#         for ogrenci in ogrenci_listesi:
#             print(f" {ogrenci}")
# def ogrenci_ara(ogrenci_listesi):
#     isim = (input("Hangi öğrenciyi arıyorsunuz: "))
#     if isim in ogrenci_listesi:
#         print(f"{isim} bu öğrenci listede bulunuyor.")
#     else:
#         print(f"{isim} bu kişi listede yok.")
    
# while True:
#     print("\n1: Öğrenci ekle")
#     print("2: Öğrenci Sil")
#     print("3: Listeyi göster")
#     print("4: Öğrenci ara")
#     print("5: Çıkış yap.")
#     secim = input("işlem seçin.")

#     if secim == "1":
#         ogrenci_ekle(ogrenci_listesi)
#     elif secim == "2":
#         ogrenci_sil(ogrenci_listesi)
#     elif secim == "3":
#         liste(ogrenci_listesi)
#     elif secim == "4":
#         ogrenci_ara(ogrenci_listesi)
#     elif secim == "5":
#         print("Programdan çıkılıyor.")
#         break
#     else:
#         print("Geçersiz seçim, lütfen tekrar deneyin.")
