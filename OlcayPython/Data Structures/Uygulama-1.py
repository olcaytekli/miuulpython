# 1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.

musteriAdi = 'Olcay'
musteriSoyad = 'Tekli'
musteriAdSoyad = musteriAdi + '' + musteriSoyad
musteriCinsiyet = True #Erkek
musteriTckimlik = '1515616662'
musteriDogumYili = 2000
musteriAdresi = 'Kadıköy'
musteriYası= 2024 - musteriDogumYili


# 2-Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.
  #SİPARİŞ 1 => 110 TL
  #SİPARİŞ 2 => 1110.5 TL
  #SİPARİŞ 3 => 356.95 TL

order1= 110
order2= 1110.5
order3= 356.95

# print (order1 + order2 + order3) böyle de yazabiliriz veya

total= order1 + order2 + order3
print ("Total:", total)
