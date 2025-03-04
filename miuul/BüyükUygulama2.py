import pandas as pd
import seaborn as sns 
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)



#Görev 1:  List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük
#harfe çeviriniz ve başına NUM ekleyiniz

df = sns.load_dataset("car_crashes")
df.columns

list = ["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]
# print(list)


# # GÖREV 2: List Comprehension yapısı kullanarak car_crashes verisindeki isminde "no" 
# barındırmayan değişkenlerin isimlerininin sonuna "FLAG" yazınız.

list1 = [col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns ]
# print(list1)


#Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden 
# FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.

og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head()


#### Pandas Alıştırmaları

# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.

df1 = sns.load_dataset("titanic")
d = df1.head()
df1.shape
# print(d)

# Görev 2: Yukarıda tanımlanan Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.

# print(df1["sex"].value_counts())

# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.

print(df1.nunique())

# Görev 4: pclass değişkeninin unique değerleri bulunuz.

print(df1["pclass"].unique())

# Görev 5:  pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.

print(df1[["pclass","parch"]].nunique())


# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz. Tekrar tipini kontrol ediniz.

print(df1["embarked"].dtype)
# print(df1["embarked"].astype("category"))


# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
print(df1[df1["embarked"] == "C"])



# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
print(df1[df1["embarked"] != "S"])

# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.

print(df1[(df1["age"] < 30) & (df1["sex"] == "female")].head(10))

# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.

print(df1[(df1["age"] > 70) | (df1["fare"] > 500 )].head(10))

# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.

df1.isnull().sum()

# Görev 12: who değişkenini dataframe'den düşürün.

df1.drop("who",axis = 1)


# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.

# df1["deck"].mode()[0]
# df1["deck"].fillna(df1["deck"].mode()[0], inplace=True)
# df1["deck"].isnull().sum()

# Görev 14: age değişkenindeki boş değerleri age değişkenin medyanı ile doldurun.
print(df1["age"].median())
print(df1["age"].fillna(df1["age"].median(),inplace = True))

# Görev 15: survived değişkeninin Pclass ve Cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.

print(df1.groupby(["sex","pclass"]).agg({"survived":["mean","sum","count"]}))

# Görev 16:  30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazınız.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)

def age_30(age):
    if age < 3:
        return 1
    else:
        return 0
    
df1["age_flag"] = df1["age"].apply(lambda x : age_30(x))


df1["age_flag"] = df1["age"].apply(lambda x: 1 if x<30 else 0)

# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.

df2 = sns.load_dataset("tips")
print(df2)

# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill  değerlerinin toplamını, min, max ve ortalamasını bulunuz.

print(df2.groupby("time").agg({"total_bill":["sum","min","max","mean"]}))


# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
print((df2.columns))
print(df2.groupby(["day","time"]).agg({"total_bill":["sum","min","max","mean"]}))


# Görev 20:Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.

print(df2[(df2["time"] == "Lunch") & (df2["sex"] == "Female")].groupby("day").agg({"total_bill": ["sum","min","max","mean"],
                                                                           "tip":  ["sum","min","max","mean"]}))
# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir?

df2.loc[(df2["size"] < 3) & (df2["total_bill"] >10 ) , "total_bill"].mean() # 17.184965034965035

# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturun. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
df2["total_bill_tip_sum"] = df2["total_bill"] + df2["tip"]



# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.

new_df = df2.sort_values("total_bill_tip_sum", ascending=False)[:30]
