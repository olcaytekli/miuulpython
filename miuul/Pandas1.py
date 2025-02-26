##### Pandas Series ####

import pandas as pd
import numpy as np

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

## Değişkenler Üzerine İşlemler ##

"age" in df  #bu değişken df'nin içinde var mı sorusu

df[["age"]].head()

df[["age","alive"]] #bir dataframeden birden fazla değişken seçmek istersek


col_names = ["age","adult_male","alive"]
df[col_names]

df["age2"] = df["age"] ** 2    #bir df'ye değişken ekleme
df["age3"] = df["age"] / df["age2"]

df.drop("age3",axis = 1)    #bir değişkeni silmek istersek
df.drop(col_names,axis = 1) #birden fazla değişkeni silmek istersek

df.loc[:, df.columns.str.contains("age")] #dflerde seçme işlemi için kullanılan özel bir yapıdır loc

# iloc & loc 

#iloc : integer based selection

df.iloc[0:3]
df.iloc[0,0]

#loc: label based selection

df.loc[0:3]


# Koşullu Seçim (Conditional Selection)

df[df["age"]> 50]  #yaşı 50den büyük
df[df["age"]> 50]["age"].count()

df.loc[df["age"]> 50,["class","age"]]  #yaşı 50den büyük olanların sınıf bilgisini getirir
df.loc[(df["age"]> 50) & (df["sex"] == "male"),["class","age"]] #parantez önemli
df.loc[(df["age"]> 50) & (df["sex"] == "male") & (df["embark_town"] == "Cherbourg"),["class","age","sex","embark_town"]]


# Toplulaştırma ve Gruplama (Aggregation & Grouping)

#toplulaştırma bize özet bilgi getirir

df["age"].mean() #yaşın ortalaması

df.groupby("sex")["age"].mean()  #cinsiyete göre yaş ortalaması
df.groupby("sex").agg({"age":["mean","sum"]}) #cinsiyete göre yaş ortalaması ve toplamı
df.groupby("sex").agg({"age":["mean","sum"],
                    "embark_town":"count"}) 
df.groupby("sex").agg({"age": ["mean","sum"],
                    "survived":"mean"})

df.groupby(["sex","embark_town"]).agg({"age": ["mean"],
                    "survived":"mean"})  

df.groupby(["sex","embark_town","class"]).agg({"age": ["mean"],
                    "survived":"mean"})  

df.groupby(["sex","embark_town","class"]).agg({
    "age": ["mean"],
    "survived":"mean",
    "sex": "count"})        

# Pivot Table                
#İstediğimiz kırılımlara göre bilgi getirebilme

df.pivot_table("survived","sex","embarked") #pivot table ortalama alır. ilk girilen değer istediğin şey diğerleri de filtreleri gibi düşün
df.pivot_table("survived","sex","embarked",aggfunc ="std")
df.pivot_table("survived","sex",["embarked","class"])  #bir boyut kazandırdım 

##hem cinsiyete hem binilen konuma hem de yaşlara göre bir kırılım istiyorsam
df["new_age"] = pd.cut[df["age"],[0,10,18,25,40,90]]    #cut belirtilen aralıklara göre sayı verileri kategorilere ayırır.
df.pivot_table("survived", "sex","new_age")  #pivot table = (istediğimiz,satır,sütun)
df.pivot_table("survived", "sex",["new_age","class"])

pd.set_option("display.width",500)  # görünümü ayarlama

# Apply ve Lambda
##Bir dataframe'e apply ile satır ve sütunlarda istediğimiz fonksiyonu uygulayabiliriz.
##Lambda bir fonksiyon şeklidir fakat kullan attır.

df["age2"] = df["age"] * 2 
df["age3"] = df["age"] * 5 

(df["age"] / 10).head()
(df["age2"] / 10).head()
(df["age3"] / 10).head()

for col in df.columns:
    if "age" in col:
        print((df[col] / 10).head())
for col in df.columns:
    if "age" in col:
        df[col] = df[col] /10
 ### apply ve lambda ile yapılış
df[["age","age2","age3"]].apply(lambda x: x/ 10)
df.loc[:,df.columns.str.contains("age")].apply(lambda x: x/ 10)

def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

df.loc[:,df.columns.str.contains("age")].apply(standart_scaler).head()
df.loc[:,["age","age2","age3"]] = df.loc[:,df.columns.str.contains("age")].apply(standart_scaler).head()   #işlemi kaydetme

# Birleştirme (Join) İşlemleri
m = np.random.randint(1,30,size = (5 ,3))

df1 = pd.DataFrame(m , columns = ["var1","var2","var3"])
df2 = df1 + 99 
## Concat
pd.concat([df1, df2],ignore_index=True)  #concat dfleri dikey veya yatay olarak birleştirir. Aynı sütunlara sahip verileri alt alta eklemek için

## Merge ile 
# not : ortak sütunlara göre birleştirir. İki veri setini belirli bir sütun üzerinden ilişkilendirmek için

df1 = pd.DataFrame({
    'employees': ['john', 'dennis', 'mark', 'maria'],
    'group': ['accounting', 'engineering', 'engineering', 'hr']
})

df2 = pd.DataFrame({
    'employees': ['mark', 'john', 'dennis', 'maria'],
    'start_date': [2010, 2009, 2014, 2019]
})

pd.merge(df1,df2) #veya pd.merge(df1,df2,on = "employees")

# Amaç: Her çalışanın müdürünün bilgisine erişmek istiyoruz.
df3 = pd.merge(df1,df2)
df4 = pd.DataFrame({
    'group': ['accounting', 'engineering', 'hr'],
    'manager': ['Caner', 'Mustafa', 'Berkcan']
})
pd.merge(df3,df4)




