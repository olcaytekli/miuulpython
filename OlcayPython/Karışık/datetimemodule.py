#Tarih ve zamanla ilgili bir işlem yapacağım zaman kullanırım.

#import datetime
# from datetime import datetime
# from datetime import date
# from datetime import time    # tek tek yapabiliriz 
from datetime import datetime 
from datetime import timedelta


simdi = datetime.now()
simdi = datetime.today() #now'la aynı bilgiyi verir

result = datetime.now()
result = simdi.year  #yukarıda şimdiyi tanımladık 
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
result = simdi.second
result = datetime.ctime(simdi)   #daha detaylı bir bilgi veriyor
result = datetime.strftime(simdi,"%Y")   #sadece yıl bilgisi
result = datetime.strftime(simdi,"%X")  #saat
result = datetime.strftime(simdi,"%d")  #gün 
result = datetime.strftime(simdi,"%A")  #gün bilgisini string olarak verir monday gibi
result = datetime.strftime(simdi,"%B")  #ay bilgisi string olarak
result = datetime.strftime(simdi,"%Y %B %A")   #harflerin karşılıklarını internette bulabilirm


# t = "10 Kasım 1938".split()  #böyle tek tek ayırabiliriz.
# print(t[0])
# print(t[1])
# print(t[2])

t = "10 November 1938 09:05:30"
result = datetime.strptime(t, "%d %B %Y %H:%M:%S")
result = result.year

birthday = datetime(2000,11,10)
result = datetime.timestamp(birthday)  #bu metotla ilgili tarih objaesi saniye cinsinden verilir
result = datetime.fromtimestamp(result)  #saniye to datetime
result = datetime.fromtimestamp(0)  #bu bilgisayarların milat tarihi yukarıda çıkan saniye cevabı da bu tarihten itibaren geçen saniye sayısı

result = simdi - birthday  #timedelta (iki tarih arasındaki fark)
# result = result.days   #timedeltadan gelen toplam gün bilgisi
result = result.seconds   #saniye bilgisi

result = simdi + timedelta(days=1000,minutes=100)  #şimdiki zamanın üstüme zaman ekliyoruz yani ileri tarihi öğreniyoruz

print(result)

