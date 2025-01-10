import pandas as pd
import numpy as np

#data
numbers = [20,30,40,50]
letters = ["a","b","c","d"]
scalar = 5
dict = {"a":10,"b":20,"c":30,"d":40}
random_numbers =np.random.randint(10,100,6)

# pandas_series = pd.Series()
# pandas_series = pd.Series(numbers)  #bilgiler indeks numarası atanarak karşımıza geliyor
# pandas_series = pd.Series(letters)  #pandas heterojen bir yapıda yani numpy gibi homojen değil. Veri tipleri aynı olmak zorunda değil
# pandas_series = pd.Series(scalar, [0,1,2,3]) #scalar bilgisi verdiğimiz indeks kadar yazılır
# pandas_series = pd.Series(numbers,["a","b","c","d"])  #numberstaki her elemana kendi key bilgimizi vermiş olduk
# pandas_series = pd.Series(dict)
# pandas_series = pd.Series(random_numbers)

pandas_series = pd.Series([20,30,40,50],["a","b","c","d"])

# result = pandas_series[0]   #20 bilgisi geliyor olmalı
# result = pandas_series[-1]  #50 gelir
# result = pandas_series[:2]  #ilk 2 eleman
# result = pandas_series[-2:]
# result = pandas_series["a"]  #20 bilgisi
# result = pandas_series["d"]  #50 bilgisi
# result = pandas_series[["a","c"]]   #20 ve 40 bilgisi. Olmayan bir key bilgisini çağırırsak mesela "e". Diğer bilgileri ekrana getirir ama e ye NaN cevabı gelir
# result = pandas_series.ndim # 1 boyutlu olduğunu söyler
# result = pandas_series.dtype   #data type gösterir. Burada int64
# result = pandas_series.shape    #cevap (4,) çıkar
# result = pandas_series.sum()    #elemanlarını toplamak için
# result = pandas_series.max()    #liste içerisindeki en büyük elemanı getirir 
# result = pandas_series.min()
# result = pandas_series + pandas_series  #liste içerisindeki elemanlar toplanır
# result = pandas_series + 50         #liste içerisindeki elemanlara 50 ekler
# result = np.sqrt(pandas_series)     #liste içerisindeki elemanların karekökünü alır

# result = pandas_series >= 50    #false veya true değerler getirir içerideki elemanlara göre
# result = pandas_series % 2 == 0


# print(pandas_series[result])    #istediğimiz koşulu sağlayan elemanları gösterir
# print(pandas_series)
# print(result)



##### ORNEK #####
opel2018 = pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel2019 = pd.Series([40,30,20,10],["astra","corsa","Grandland","insignia"])

total = opel2018 + opel2019

print(total["astra"])
# print(total["combo"]) # buna karşılık gelen bir bilgi olmadığı için hata getirir.
