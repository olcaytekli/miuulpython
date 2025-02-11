import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3),index = ["A","B","C"], columns=["Column1","Column2","Column3"])

result = df
result = df["Column1"]
result = type(df["Column1"])
result = df[["Column1","Column2"]]   #kolonlara göre seçme işlemi

### loc["row","column"] # kullanımı böyle fakat ben sadece satır seçmek istersem => loc["row"] 
# veya kolon seçmek istersem loc[":","column"]

result = df.loc["A"]    # A satırı bize bir seri olarak döndürülür
result = type(df.loc["A"])
result = df.iloc[2]
result = df.loc[:,"Column1"]
result = df.loc[:,["Column1","Column2"]]  #9.satırdaki cevapla aynı cevap
result = df.loc[:,"Column1":"Column3"] #belirli kolonları değil de aralık almak istersek (1 ve 3 dahil)
result = df.loc[:,:"Column2"]
result = df.loc["A":"B",:"Column2"]  #Satır için de aralık seçebiliriz. Indeksi biz yukarıda harflendirdik, yapmasaydık 1 2 yazabilirdik
result = df.loc[:"B",:"Column2"]
result = df.loc["A","Column2"]  #seçme işlemi
result = df.loc["C","Column1"]
result = df.loc[["A","B"],["Column1","Column2"]]

## yeni bir satır eklemek istersek

df["Column4"] = pd.Series(randn(3), ["A","B","C"])
df["Column5"] = df["Column1"] + df["Column3"]  #column5 i eklerken iki columnun toplamı olarak yazdırdık

## Colomn silmek istersek
result = df.drop("Column5", axis = 1, inplace = False)  #1 yukarıdan aşağı, 0 soldan sağa 
# inplace e true vermezsek orijinal seri üzerinde bir değişiklik yapmıyor ve sadece kopyasını çıkartıyor

print(result)
print(df)

