#### IF, ELSE, ELIF ALIŞTIRMALARI ####

'''
1. Kullanıcıdan Yaş Bilgisi Alarak İzin Verme
Kullanıcının yaşını soran ve belirli yaş aralıklarına göre farklı izinler veren bir örnek.
0-14 yaş arası: çocuklar ve ergenler
15-64 yaş arası: aktif nüfus veya çalışan nüfus
65 ve üzeri: yaşlı ve bağımlı nüfus

'''
# def yas_araliklari(yas):

#     if 0 < yas <= 14:
#         print("Çocuklar ve ergenler sınıflandırması.")
#     elif 15 <= yas <= 64:
#         print("Aktif nüfus veya çalışan nüfus sınıflandırması.")
#     elif yas >= 65:
#         print("Yaşlı sınıflandırması. ")
#     else: 
#         print("Yanlış bir değer girdiniz.")

# yas = int(input("Yaşınız girin: "))
# yas_araliklari(yas)



'''
2. Saat Dilimi ve Günün Zamanına Göre Selamlaşma 
Kullanıcıdan saat bilgisini alarak günün zamanına göre uygun bir selamlaşma mesajı yazan bir örnek.
'''
# def greeting(hour):
#     if 6 < hour < 11:
#         print("Günaydın!")
#     elif 11 <= hour < 18:
#         print("İyi öğlenler")
#     elif 18 <= hour < 22:
#         print("İyi akşamlar")

# hour = int(input("Saat kaç ? "))
# greeting(hour)





'''
3. Birim Fiyatına Göre İndirim Uygulama
Bir ürünün fiyatını alıp, belirli bir fiyat aralığına göre indirim uygulayan bir örnek.
'''

def discount(cost):
    print("Belirli fiyat aralığına indirim uygulanacaktır.")
    if 0< cost <= 100:
        print("Harcamanıza indirim uygulanmayacaktır.")
    elif 100 < cost <= 500:
        indirim = cost * 0.80
        print(f"%20 indirim uygulanmıştır. Ödeyeceğiniz miktar : {indirim}")
    elif cost > 500:
        indirim1 = cost * 0.60
        print(f"% 40 indirim uygulanmıştır. Ödeyeceğiniz miktar: {indirim1}")
    else:
        cost < 0
        print("Yanlış bir değer girdiniz.")

cost = int(input("Harcamanızı girin: "))
discount(cost)
    




#### FOR DÖNGÜSÜ ####
'''
1. Alışveriş Listesindeki Ürünleri Yazdırma
Bir alışveriş listesinde bulunan ürünleri yazdırmak için for döngüsü kullanabilirsiniz.
alisveris_listesi = ["Ekmek", "Süt", "Peynir", "Yumurta", "Elma"]. Her ürünü yazdıralım.
'''

'''
2. Saatlik Aktivite Planı
Bir gün boyunca yapılacak aktiviteleri saat saat listeleyip yazdırmak için for döngüsü kullanabilirsiniz.
aktivite_planı = [
    "07:00 - Kahvaltı",
    "08:00 - İşe başlama",
    "12:00 - Öğle yemeği",
    "15:00 - Ara",
    "18:00 - Eve dönüş",
    "20:00 - Akşam yemeği",
    "22:00 - Uyuma"
]
'''

'''
3. Sınıftaki Öğrencilerin Notlarını Yazdırma
Bir sınıftaki öğrencilerin isimlerini ve notlarını yazdırmak için for döngüsü kullanılabilir.
ogrenci_notları = {"Ali": 85, "Ayşe": 92, "Mehmet": 78, "Zeynep": 88}
'''

'''
4. Kredi Kartı Harcama Özetini Yazdırma
Bir kişinin kredi kartı harcamalarını listeleyip toplam harcamayı hesaplamak için for döngüsü kullanılabilir.
harcamalar = [50, 100, 200, 75, 120]
'''

### WHILE DÖNGÜSÜ ###

'''
1. Kullanıcıdan Doğru Şifreyi Alana Kadar Girdi Alma
Bir uygulamada kullanıcıdan doğru şifreyi girene kadar şifre girmesi istenebilir. Bu işlem için while döngüsü kullanılır.
dogru_sifre = "1234"
'''

'''
2. Kullanıcıdan Pozitif Bir Sayı İsteme
Kullanıcıdan pozitif bir sayı girmesi istenebilir. Kullanıcı yanlış bir sayı girerse, doğru sayıyı girene kadar tekrar istenebilir.
'''

'''
3. Kullanıcıdan 0'ı Girmesiyle Durdurulan Harcama Listesi
Bir kişinin yaptığı harcamalar listelenip, kullanıcı 0'ı girdiğinde listeleme durdurulabilir.
'''

'''
4. Kullanıcının Sayı Girerek Toplama Yapması
Kullanıcıdan sürekli sayı girmesi istenebilir ve bu sayılar toplanır. 0 girildiğinde işlem sonlandırılır.
'''

'''
5. Sınıfın Ortalama Notunu Hesaplama
Bir sınıftaki öğrencilerin notlarını girip, ortalamayı hesaplayabilirsiniz. Kullanıcı 0 girene kadar notları almaya devam eder.
'''