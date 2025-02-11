# # website = "http://www.sadikturan.com"
# # course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

# # # 1.Soru " Hello World " karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

# # # result = " Hello World ".strip()
# # # print(result)

# # # result = "Hello World ".lstrip("Hello")
# # # print(result)

# # # 2.soru "www.sadikturan.com" içindeki sadikturan bilgisi haricindeki her karakteri silin.

# # result = website.strip("htp/:wcom.")
# # print(result)

# # # 3.Soru "course" karakter dizisinin tüm karakterlerini küçük harf yapın.

# # result = course.lower()
# # print(result)

# # # 4.Soru "website" içinde kaç tane a karakteri vardır? (count("a"))
# # result = website.count("a")

# # # 5.Soru "website"  "www" ile başlayıp "com" ile bitiyor mu?
# # result = website.startswith("www")
# # result1 = website.endswith("com")

# # #7.Soru "course" içindeki karakterlerin hepsi alfabetik mi? (isalpha(alfabetik mi),isdigit(rakam mı))

# # result = course.isalpha()

# # 1.Soru "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.

# markalar = ["Bmw","Mercedes","Opel","Mazda"]


# # # 2.Soru Liste Kaç Elemanlıdır?

# # length = len(markalar)
# # print(length)

# # # 3.Soru Listenin ilk ve son elemanı nedir?

# # print(markalar[0])
# # print(markalar[length-1])


# # # 4.Soru Mazda değerini Toyota ile değiştirin.
# # markalar[3] = "Toyota"

# # 5.Soru Mercedes listenin bir elemanı mıdır?

# isEleman = "Mercedes" in markalar
# print(isEleman)

# # 6. Soru Listenin -2 indeksindeki değer nedir?

# print(markalar[-2])


# # 7.Soru Lisenin ilk 3 elemanını alın.

# # print(markalar[0:3])

# # # 8.Soru Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.

# # markalar[-2:] = "Toyota","Renault"

# # # 9.Soru Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
# # list = markalar + ["Audi", "Nissan"]
# # print(list)

# # 10.Soru Listenin son elemanını silin.

# # list = markalar.pop()
# # print(list)

# # 11.Soru Liste elemanlarını tersten yazdırın.


# # print(markalar[::-1])


# # print(markalar)



# names = ["Ali","Yağmur","Hakan","Deniz"]
# years = [1998,2000,1998,1987]

# 1.Soru "Cenk" ismini listenin sonuna ekleyiniz.

# names.append("Cenk")
# print(names)

# # 2.Soru "Sena" değerini listenin başına ekleyiniz.

# names.insert(0,"Sena")
# print(names)

# 3.Soru "Deniz" ismini listeden siliniz.

# names.remove("Deniz")
# print(names)

# # 4.Soru "Deniz" isminin indexi nedir?

# index = names.index("Deniz")
# print(index)

# # 5.Soru "Ali" listenin bir elemanı mıdır?

# isFound = "Ali" in names
# print(isFound)

# 6.Soru Liste elemanlarını ters çevirin.

# names.reverse()
# print()

# 7.Soru Liste elemanlarını alfabetik olarak sıralayınız.

# names.sort()
# print(names)

# # 8.Soru str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
# str = "Chevrolet,Dacia"

# message = str.split(",")
# print(message)

# # 9.Soru years dizisinin en büyük ve en küçük elemanı nedir?

# value = min(years)
# value1 = max(years)

# print(value, value1)

# # 10.Soru years dizisinde kaç tane 1998 değeri verdır?

# sayı = years.count(1998)
# print(sayı)

# 11.Soru years dizisinin tüm elemanlarını silin.

# years.clear()
# print(years)


# # 12.Soru Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
# markalar = []

# marka = input("Marka ismi: ")
# markalar.append(marka)

# marka = input("Marka ismi: ")
# markalar.append(marka)

# marka = input("Marka ismi: ")
# markalar.append(marka)

# print(markalar)


# # 1. Kullanıcıdan 3 Sayı Al ve Listele

# sayılar = []

# sayı = float(input("Sayı giriniz:  "))
# sayılar.append(int(sayı))

# sayı = float(input("Sayı giriniz:  "))
# sayılar.append(int(sayı))

# sayı = float(input("Sayı giriniz:  "))
# sayılar.append(int(sayı))



# print(sayılar)


# sayilar = []  # Boş bir liste oluştur

# sayi1 = int(input("1. sayıyı giriniz: "))
# sayilar.append(sayi1)  # İlk sayıyı listeye ekle

# sayi2 = int(input("2. sayıyı giriniz: "))
# sayilar.append(sayi2)  # İkinci sayıyı listeye ekle

# sayi3 = int(input("3. sayıyı giriniz: "))
# sayilar.append(sayi3)  # Üçüncü sayıyı listeye ekle

# print("Girdiğiniz sayılar:", sayilar)

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

students = {}

number = input("Öğrencinin numarasını girin: ")
names = input("Öğrencinin adını girin: ")
surname = input("Öğrencinin Soyadını girin: ")

students.update({ 
            number: {
                "ad": names,
                "soyad": surname  
            }
})

number = input("Öğrencinin numarasını girin: ")
names = input("Öğrencinin adını girin: ")
surname = input("Öğrencinin Soyadını girin: ")

students.update({ 
            number: {
                "ad": names,
                "soyad": surname  
            }
})


print(students)


#   2.Soru      Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgilerini ekrana getirin.

numara = input("Öğrencinin numarasını girin:")

ogrenci =students[numara]
print(ogrenci)