"""
    ogrenciler = {
        "120": {
            "ad": "Ali",
            "soyad": "Yılmaz",
            "telefon": "532 000 00 01
        },
         "125":{
            "ad": "Can",
            "soyad":"Korkmaz",
            "telefon":"532 000 00 02"
        },
        "128":{
            "ad":"Volkan",
            "soyad":"Yükselen",
            "telefon":"532 000 00 03"
        },
        
    }
""" 

# 1.Soru     Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.

ogrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrencinin soyadı: ")
telefon = input("öğrencinin telefon numarası: ")

# ogrenciler[number] = {
#     "ad" : name,
#     "soyad" : surname,
#     "telefon" : telefon,

# }                      ###bunların aynısını update metoduyla da yapabiliriz.

ogrenciler.update({
    number: {
        "ad": name,
        "soyad": surname,
        "telefon": telefon
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrencinin soyadı: ")
telefon = input("öğrencinin telefon numarası: ")

ogrenciler.update({
    number: {
        "ad": name,
        "soyad": surname,
        "telefon": telefon
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrencinin soyadı: ")
telefon = input("öğrencinin telefon numarası: ")

ogrenciler.update({
    number: {
        "ad": name,
        "soyad": surname,
        "telefon": telefon
    }
})


print(ogrenciler)


#   2.Soru      Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgilerini ekrana getirin.

ogrNo = input("öğrenci no: ")
ogrenci = ogrenciler[ogrNo]
print[ogrenci]