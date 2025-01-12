import pandas as pd
import numpy as np

data = {
    "Column1":[1,2,3,4,5,],
    "Column2":[10,20,13,45,25],
    "Column3":["abc","bcaa","ade","cb","dea"]
}

df = pd.DataFrame(data)

def kareal(x):
    return x * x

kareal12 = lambda x: x * x

result = df
result = df["Column2"].unique()     #tekrarlayanları getirmez
result = df["Column2"].nunique()    #tekrarlamayanların sayısı gelir
result = df["Column2"].value_counts()   #hangi sayıdan kaç tane var gösterir
result = df["Column1"] * 2      #elemanları 2yle çarpılır
result = df["Column2"].apply(kareal)
result = df["Column2"].apply(lambda x: x* x)
result = df["Column2"].apply(kareal12)
result = df["Column3"].apply(len)   #her bir elemanın kaç karakterli olduğu
df["Column4"] = result = df["Column3"].apply(len)  # bilgiyi column4 e atabiliriz

result = df.columns
result = len(df.columns)    # columns sayısı
result = df.index
result = len(df.index)
result = df.info

result = df.sort_values("Column2")
result = df.sort_values("Column3")
result = df.sort_values("Column3",ascending=False)  #ascending yaparsak tam tersi bir şekilde sıralar

data = {
    "Ay":["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori" : ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20,30,15,14,32,42,12,36,52]
}

df = pd.DataFrame(data)
df = df.pivot_table(index ="Ay",columns = "Kategori",values = "Gelir")

print(df)
# print(result)