#   BANKAMATİK UYGULAMASI
SadikHesap = {
    "ad":"Sadık Turan",
    "hesapNo": "12345678",
    "bakiye": 3000,
    "ekHesap": 2000
}
AliHesap = {
    "ad":"Ali Turan",
    "hesapNo": "456789",
    "bakiye": 2000,
    "ekHesap": 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap["ad"]}")

    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print("paranızı alabilirsiniz.")
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]
        if (toplam >= miktar):
            ekHesapKullanimi = input("ek hesap kullanılsın mı (e/h)")

            if ekHesapKullanimi == "e":
                bakiye = hesap["bakiye"]
                ekhesapKullanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0  #ek hesaba geçiyorsak bakiye sıfırlanması gerekir.
                hesap["ekHesap"] -= ekhesapKullanilacakMiktar
                print("paranızı alabilirsiniz.")
            else:
                print(f"{hesap["hesapNo"]} olu hesabınızda {hesap["bakiye"]} bulunmaktadir.")
        else: 
            print("Üzgünüz bakiye yetersiz.")    

def bakiyeSorgula(hesap):
    print(f"{hesap["hesapNo"]} nolu hesabınızda {hesap["bakiye"]} TL bulunmaktadır.Ek hesap liminitiniz ise {hesap["ekHesap"]}TL bulunmaktadır.")
#bakiye sorgulamayı para çekme işlemlerinden sonra da sorgulayabiliriz yani 20.satırdan sonra
paraCek(SadikHesap,2000)
bakiyeSorgula(SadikHesap)
print("********")
paraCek(SadikHesap,3000)
bakiyeSorgula(SadikHesap)