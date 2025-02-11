# 1 - Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.
# Ehliyet alma koşulu en az 18 yaş ve eğitim durumu lise ya da üniversite olmalıdır.

# isim = input("İsminizi girin: ")
# yaş = int(input("Yaşınızı girin: "))
# eğitim = input("Eğitim bilginizi girin: ")

# if (yaş >= 18) and ((eğitim.lower() == "lise") or (eğitim.lower() == "üniversite")):
#     print("Ehliyet alabilirsiniz.")

# else:
#     print("Ehliyet alamazsınız.")


###Neden alamazsın sorusu için alternatif kod.

# isim = input("İsminizi girin: ")
# yaş = int(input("Yaşınızı girin: "))
# eğitim = input("Eğitim bilginizi girin: ")

# if (yaş >= 18):
#     if ((eğitim.lower() == "lise") or (eğitim.lower() == "üniversite")):
#         print(f"{isim} Ehliyet alabilirsiniz.")
#     else:
#         print("Ehliyet alamazsınız eğitim durumunuz yetersiz.")
# else:
#     print("Yaşınızdan dolayı ehliyet alamazsınız.")




# 2 - Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre 
# not aralığına karşılık gelen not bilgisini yazdırınız.

# 0 - 24 => 0
# 25 - 44 => 1
# 45 - 54 => 2
# 55 - 69 => 3
# 70 - 84 => 4
# 85 - 100 => 5

# not1 = int(input("1.Notunuzu girin: "))
# not2 = int(input("2.Notunuzu girin: "))
# sözlü = int(input("Sözlü notunuzu girin: "))

# ortalama = ((not1 + not2 + sözlü) / 3 )

# if 0 <= ortalama <= 24: 
#     print(f"Ortalamanız: {ortalama} Not aralığınız: 0 ")
# elif 25 <= ortalama <= 44:
#     print(f"Ortalamanız: {ortalama} Not aralığınız: 1")
# elif 45 <= ortalama <= 54:
#     print(f"Ortalamanız: {ortalama} Not aralığınız: 2")
# elif 55 <= ortalama <= 69:
#     print(f"Ortalamanız: {ortalama} Not aralığınız: 3")
# elif 70 <= ortalama <= 84:
#     print(f"Ortalamanız: {ortalama} Not aralığınız: 4")
# elif 85 <= ortalama <= 100:
#     print(f"Ortalamanız: {ortalama} Not aralığınız: 5")
# else:
#     print("Yanlış bilgi girdiniz.")









# 3 - Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki 
# bilgilere göre hesaplayınız.

# 1.Bakım => 1.yıl
# 2.Bakım => 2.yıl
# 3.Bakın => 3.Yıl
#       **Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
#       *** datetime modülünü kullanmanız gerekiyor.

# import datetime
# tarih = input("aracınız hangi tarihte trafiğe çıktı: ")
# tarih = tarih.split("/")
# trafigecikis = datetime.datetime(int(tarih[0],int(tarih[1],int(tarih[2]))))
# simdi = datetime.datetime.now()
# fark = simdi - trafigecikis
# days = fark.days


# if days <= 365:
#     print("1.servis aralığı")
# elif days > 365 and days <= 365*2 :
#     print("2.servis aralığı")  
# elif days > 365*2 and days <= 365*3:
#     print("3.servis aralığı")




# 1 - Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

# sayi = int(input("Sayı girin: "))

# if 0 < sayi < 100:
#      print(f"{sayi} Sayısı 0 ve 100 arasındadır.")

# else:
#     print(f"{sayi} sayısı 0 ve 100 arasında değildir.")




# 2 - Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

# sayi = int(input("Sayı girin: "))

# if sayi > 0:
#     if sayi % 2 == 0:
#         print("Sayı çift ve pozitiftir.")
#     else:
#         print("Sayı çift değil.")
# else:
#     print("Sayı pozitif değil")


#3 - Email ve parola bilgileri ile giriş kontrolü yapınız.

# email = "olcay@hotmail.com"
# şifre = "123456"

# mail = input("Bir mail girin:")
# password = input("Bir şifre girin:")

# if mail.lower() == email.lower():
#     if password == şifre:
#         print("Giriş başarılı!")
#     else:
#         print("Şifreniz yanlış. Giriş başarısız!")
# else:
#     print("Mailiniz yanlış. Giriş başarısız!")

# 4 - Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

# a = int(input("1.Sayıyı girin: "))
# b = int(input("2.Sayıyı girin: "))
# c = int(input("3.Sayıyı girin: "))

# if (a > b) and ( a > c): 
#     print(f"a en büyük sayıdır")

# elif (b > a) and ( b > c): 
#     print(f"b en büyük sayıdır")

# elif  (c > a) and ( c > b):
#     print(f"c en büyük sayıdır")

# 5 - Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
# Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# vize1 = int(input("1.vize notunuzu girin: "))
# vize2 = int(input("2.vize notunuzu girin: "))
# final = int(input("Final notunuzu girin: "))

# ortalama = ((vize1 + vize2 )/2 * 0.6) + (final * 0.4)
# sonuç = (ortalama >= 50)

# if sonuç:
#     print(f"Dersi geçtiniz.")
# else:
#     print("Kaldınız.")


# a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.

# if (sonuç):
#     if (final >= 50 ):
#         print("Geçtiniz.")
#     else:
#         print("Final notunuz en az 50 olmalı. Kaldınız.")
# else:
#     print("Ortalamanız geçmeniz için yetmedi.")


# b-) Finalden 70 alındığında ortalamanın önemi olmasın.

# if (ortalama >= 50):
#     print("Geçtiniz.")

# else: 
#     if (final >= 70):
#         print("Final notunuz 70 ve üstü olduğu için geçtiniz.")
#     else: 
#         print("Kaldınız.")


# 6 - Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
# Formül: (Kilo / boy uzunluğunun karesi)
# Aşağıdaki tabloya göre kişi hangi gruba girmektedir.

# 0-18.4 => Zayıf
# 18.5-24.9 => Normal
# 25.0-29.9 => Fazla Kilolu
# 30.0-34.9 => Şişman (Obez)

# Kilo = float(input("Kilonuzu giriniz: "))
# Boy = float(input("Boyunuzu giriniz: "))

# bmi = (Kilo ) / (Boy ** 2)

# if (bmi >=0) and (bmi <= 18.4):
#     print(f" Kilo indeksin: {bmi} ve zayıfsınız.")
# elif (bmi >18.4) and (bmi <= 24.9):
#     print(f" Kilo indeksin: {bmi} ve kilo değerlendirmen: Normal")
# elif (bmi >24.9) and (bmi <= 29.9):
#     print(f" Kilo indeksin: {bmi} ve kilo değerlendirmen: Kilolu")
# elif (bmi >29.9) and (bmi <= 34.9):
#     print(f" Kilo indeksin: {bmi} ve kilo değerlendirmen: Obez")




    


