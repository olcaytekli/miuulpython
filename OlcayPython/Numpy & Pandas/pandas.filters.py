# DataFrame Filtreleme

import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data,columns=["Column1","Column2","Column3","Column4","Column5"])


result = df
result = df.columns
result = df.head()  #ilk 5 kaydı çağırabiliriz
result = df.head(10)    #ilk 10 kayıt gelir
result = df.tail()  #son 5 kaydı getirir
result = df.tail(10)    #son 10 kaydı getirir

# istediğimiz bir columnı almak istersek
result = df["Column1"].head()   #sadece column1deki ilk 5 kaydı getirir
result = df.Column1.head()  #yukarıdakiyle aynı cevabı getirir

#birden fazla kolon almak istersek
result = df[["Column1","Column2"]]  #sadece column 1 ve 2 bilgisi gelir. 
result = df[["Column1","Column2"]].head()  #sadece column 1 ve 2 bilgisi gelir ve sadece ilk 5 bilgi gelir
result = df[["Column1","Column2"]].tail() #sadece column 1 ve 2 bilgisi gelir ve son 5 bilgiyi getirir

#dataframi parçalama işlemi
result = df[5:15][["Column1","Column2"]].head() #girdiğimiz koşuldaki ilk 5 bilgiyi aldık
result = df[5:15][["Column1","Column2"]].tail() #girdiğimiz koşuldaki son 5 bilgiyi aldık

#bir filtreleme işlemi nasıl yapılır?
result = df > 50  #dataframedeki bilgilerden hangisi 50'den büyükse true bilgisi çıkarır
result = df[df > 50]    #dataframedeki bilgilerin içinden 50 den büyük olanları gösterir diğerleri NaN der
result = df[df % 2 == 0]
result = df["Column1"] > 50 #sadece column1deki 50den büyük değerlere true getirir
result = df[df["Column1"] > 50]
result = df[df["Column1"] > 50][["Column1","Column2"]] #column1 için 50 den büyükler gelir buna karşılık olarak da column2 koşulsuz gelir
result = df[(df["Column2"]>50) & (df["Column1"]< 70)]
result = df[(df["Column1"]>50) & (df["Column2"]<= 70)]
result = df[(df["Column1"]>50) | (df["Column2"]<= 70)]  # or demek
result = df[(df["Column1"]>50) | (df["Column2"]<= 70)][["Column1","Column2"]]  # sadece 1 ve 2.columnu getirir
result = df.query("Column1 >=50 & Column1 % 2 == 0") 
result = df.query("Column1 >=50 & Column1 % 2 == 0")[["Column1","Column2"]] 




print(result)