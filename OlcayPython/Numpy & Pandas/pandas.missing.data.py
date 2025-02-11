## eksik veya yanlış veri ile çalışmak 

import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data,index = ["a","c","e","f","h"],columns = ["column1","column2","column3"])

df = df.reindex(["a","b","c","d","e","f","g","h"])

newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]   #yeni colomn oluşturmak için
df["column4"] = newColumn

result = df
result = df.drop("column1",axis = 1)     # axis 1se kolon, 0ysa sütun silinir
result = df.drop(["column1","column2"],axis = 1) #birden fazla silmek istersek
result = df.drop("a",axis = 0) # a satırını silmek için
result = df.drop(["a","b","h"],axis = 0) 

result = df.isnull()  # NaN olanlara True , diğerlerine false değeri getirir
result = df.notnull()   #tam tersi NaN olanlar false diğerleri true
result = df.isnull().sum() #NaN ların toplam sayısını verir
result = df["column1"].isnull().sum() #sadece column1deki NaN miktarı
result = df[df["column1"].isnull()] #column1den NaN değerlerini getir.
result = df[df["column1"].isnull()]["column1"]  #sadece column1dekileri getir
result = df[df["column1"].notnull()]["column1"] #Nan olmayanları getir sadece column1

result = df.dropna()    #droptan farkı NaN olan satırları silmesi. varsayılan axis değeri sıfır
result = df.dropna(axis=1) #NaN barındıran sütunları siler
result = df.dropna(how = "any")  # Herhangi bir NaN değer görürse siler
result = df.dropna(how ="all") # Tüm satır olduğu gini NaN sa siler
result = df.dropna(subset = ["column1","column2"],how="all") #NaN ı belirttiğim columnlarda ara ve sil
result = df.dropna(subset = ["column1","column2"],how="any")
result = df.dropna(thresh = 2)  # en az 2 tane kayıt varsa onları silme
result = df.dropna(thresh = 4)  # en az 4 tane normal veri varsa silme geri kalanını sil

result = df.fillna(value = "No input")  #NaN olan yerleri fill metotu doldursun
result = df.fillna(value = 1)

result = df.sum()
result = df.sum().sum()
result = df.size   #eleman sayısı gelir
result = df.isnull().sum().sum()   #toplam NaN değerini  gösterir(burada 13)



def ortalama (df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam / adet

result = df.fillna(value = ortalama(df))


print(result)
print(df)