##### Pandas Series ####

import pandas as pd

r = pd.Series([10,77,12,4,5,6])
print(r)

r.size # boyutunu söyler
r.dtype # tipini söyler
r.ndim  # boyutunu söyler
r.values #içindeki değerlere erişme
r.head() #içindeki ilk 5 değeri getirir
r.tail() #sondan 5

# Veri Okuma (Reading Data)

# df = pd.read_cvs(".......")


#Veriye Hızlı Bir Bakış
import seaborn as sns

df = sns.load_dataset("titanic")
print(df.head())
print(df.info()) #değişkenler hakkında bilgi verir
print(df.columns) # değişkenleri gösterir
print(df.index) #index bilgisi verir
print(df.describe().T)  #betimsel istatiklerini getirir
print(df.isnull().sum())    #her bir değerdeki eksik ifade sayısını gösterir
df["sex"].head()  # bir df den bilgi çekmek istediğimizde


#Pandas'ta Seçim İşlemleri (Selection in Pandas) 

df.index  #index işlemi için
df[0:13] #dilimleme  işlemi 
df.drop(0,axis=0)  #Silme işlemi , satır = 0 ve 0.indeksi silmek için

delete_indexes = [1,3,5,7]
df.drop(delete_indexes,axis=0) #birden fazla silmek istersek
df.drop(delete_indexes,axis=0,inplace=True) #bu değişikliği kalıcı hale getirmek için

#Değişkeni Indexe Çevirmek

df["age"].head()
df.age.head()

df.index = df["age"]
df.drop("age",axis =1,inplace=True)

#Indexi değişkene çevirme

df.index
df["age"] = df.index


df.reset_index()  #resetleme