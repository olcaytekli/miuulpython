#Görev 2:  Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, 
#kelime kelime ayırınız.

text = "The goal is to turn data into information, and information into insight."

r = text.upper().replace(".", " ").replace("," ," ").split(" ")
print(r)

# Görev 3:  Verilen listeye aşağıdaki adımları uygulayınız.
#  Adım1: Verilen listenin eleman sayısına bakınız.
#  Adım2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
#  Adım3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
#  Adım4: Sekizinci indeksteki elemanı siliniz.
#  Adım5: Yeni bir eleman ekleyiniz.
#  Adım6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

print(len(lst))

print(lst[0],lst[10])

print(lst[0:4])

print(lst.pop(8))

lst.append(101)
print(lst)

lst.insert(8,"N")
print(lst)



# Görev 4:  Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
#  Adım1: Key değerlerine erişiniz.
#  Adım2: Value'lara erişiniz.
#  Adım3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
#  Adım4: Key değeriAhmet value değeri[Turkey,24] olan yeni bir değer ekleyiniz.
#  Adım5: Antonio'yu dictionary'den siliniz.

dict = {
    "Christian": ["America",18],
    "Daisy": ["England",12],
    "Antonio": ["Spain",22],
    "Dante":["Italy",25]
        }

dict.keys()

dict.values()

dict.update({"Daisy": ["England",13]})

dict["Daisy"][1] = 14

dict.update({"Ahmet": ["Turkey",24]})
dict.pop("Antonio")

print(dict)


# Görev 5:Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri
# return eden fonksiyon yazınız.

l = [2,13,18,93,22]

def func(list):
    list1 = []
    list2 = []

    for x in l:
        if x % 2 == 0:
            list1.append(x)
        else:
            list2.append(x)
    return list1 , list2 

print(func(l))



#  Görev 6:Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri
#  bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de 
# tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

for index,ogrenci in enumerate(ogrenciler):
    if index < 3:
        index +=1
        print(f"Mühendislik fakültesi", index , "ogrenci:", ogrenci )
    else: 
        index -= 2
        print("Tıp fakültesi", index, "ogrenci",ogrenci)


# Görev 7:Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer
#  almaktadır. Zip kullanarak ders bilgilerini bastırınız

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

for ders_kodu,kredi,kontenjan in zip(ders_kodu,kredi,kontenjan):
    print(f"kredisi {kredi} olan{ders_kodu}kodlu dersin kontenjanı {kontenjan} kişidir.")

# Görev 8:Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını
#  eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def kume(set1, set2):
    if set1.issuperset(set2):  # Hatalı olan 'set' yerine 'set2' yazıldı
        return set1.intersection(set2)  # print yerine return kullanıldı
    else:
        return set2.difference(set1)  # print yerine return kullanıldı

print(kume(kume1, kume2))  # kume1, kume2'yi kapsamıyor, farkı yazdırır
print(kume(kume2, kume1))  # kume2, kume1'i kapsadığı için ortak elemanları yazdırır
