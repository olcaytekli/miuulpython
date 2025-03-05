##### Gelişmiş Fonksiyonel Keşifçi Veri Analizi (Advanced Functional EDA)

### 1. Genel Resim ###

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns" , None)
pd.set_option("display.width" , 500)
df = sns.load_dataset("titanic")
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any() # eksik değer var mı yok mu
df.isnull().sum() #eksik değer sayısı


def check_df(dataframe, head = 5):
    print("######### Shape #######")
    print(dataframe.shape)
    print("######### Types #######")
    print(dataframe.dtypes)
    print("######### Head #######")
    print(dataframe.head(head))
    print("######### Tail #######")
    print(dataframe.tail(head))
    print("######### NA #######")
    print(dataframe.isnull().sum())
    print("######### Quantiles #######")
    print(dataframe.describe([0, 0.05 , 0.50, 0.95, 0.99, 1]).T)


check_df(df)


# df1 = sns.load_dataset("flights")
# def check_df(dataframe, head = 5):


# check_df(df1)



### 2. Kategorik Değişken Analizi (Analysis of Categorical Variables) ###

df["embarked"].value_counts()
df["sex"].unique()
df["class"].nunique()


cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category","object","bool"]]

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int","float"]]

cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category","object"]]

cat_cols = cat_cols + num_but_cat

cat_cols = [col for col in cat_cols if col not in cat_but_car]
df[cat_cols].nunique()
cols= [col for col in df.columns if col not in cat_cols]


df["survived"].value_counts()
100 * df["survived"].value_counts() / len(df)

def cat_summary(dataframe,col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_count(),
                        "Ratio": 100 * dataframe[col_name].value_counts()/len(dataframe)}))
    print("##################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

cat_summary(df,"sex", plot=True)


for col in cat_cols:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)
        cat_summary(df,col,plot=True)
        print("sdasdsadsasads")
    else:
        cat_summary(df,col,plot=True)


df["adult_male"].astype(int)

for col in cat_cols:
    if df[col].dytpes == "bool":
        # df[col] = df[col].astype(int)

        cat_summary(df,col,plot=True)
    
    else:
        cat_summary(df,col,plot =True)



### 3. Sayısal Değişken Analizi (Analysis of Numerical Variables) ###

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()


cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object","bool"]]
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int","float"]]
cat_but_car = [col for col in df.columns if df[col].nunique()> 20 and str(df[col].dtypes) in ["category", "object"]]
cat_cols = cat_cols + num_but_cat
cat_cols = [col for col in cat_cols if col not in cat_but_car]

df[["age","fare"]].describe().T
num_cols=[col for col in df.columns if df[col].dtypes in ["int","float"]]
num_cols=[col for col in num_cols if col not in cat_cols]

def num_summary(dataframe, numerical_col):
    quantiles = [0.05,0.10,0.20,0.30,0.40,0.50,0.60,0.80]
    print(dataframe[numerical_col].describe(quantiles).T)

num_summary(df,"age")

for col in num_cols:
    num_summary(df,col)

def num_summary(dataframe, numerical_col,plot):
    quantiles = [0.05,0.10,0.20,0.30,0.40,0.50,0.60,0.80]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)
num_summary(df,"age",plot=True)

for col in num_cols:
    num_summary(df,col,plot=True)


def cat_summary(dataframe,col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_count(),
                        "Ratio": 100 * dataframe[col_name].value_counts()/len(dataframe)}))
    print("##################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

for col in cat_cols:
    cat_summary(df,col,plot=True)

for col in num_cols:
    num_summary(df,col,plot=True)


### Değişkenlerin Yakalanması ve İşlemlerin Genelleştirilmesi ###

def grap_col_names(dataframe, cat_th=10,car_th=20):
    """   Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini döndürür.


Parameters  
-----------  
dataframe: dataframe  
    değişken isimleri alınmak istenen dataframe'dir.  
cat_th: int, float  
    numerik fakat kategorik olan değişkenler için sınıf eşik değeri  
car_th: int, float  
    kategorik fakat kardinal değişkenler için sınıf eşik değeri  

Returns  
-------  
cat_cols: list  
    Kategorik değişken listesi  

num_cols: list  
    Numerik değişken listesi  

cat_but_car: list  
    Kategorik görünümlü kardinal değişken listesi  """
    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object","bool"]]
    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int","float"]]
    cat_but_car = [col for col in df.columns if df[col].nunique()> 20 and str(df[col].dtypes) in ["category", "object"]]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]
    num_cols = [col for col in df.columns if df[col].dtypes in ["int","float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]
    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f"cat_cols: {len(cat_cols)}")
    print(f"Observations: {len(num_cols)}")
    print(f"Observations: {len(cat_but_car)}")
    print(f"Observations: {len(num_but_cat)}")

    return cat_cols,num_cols,cat_but_car
cat_cols,num_cols,cat_but_car = grap_col_names(df)

def cat_summary(dataframe,col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                     "Ratio": 100*dataframe[col_name].value_counts()   }))
    print("################")
cat_summary(df,"sex")

for col in cat_cols:
    cat_summary(df,col)

def num_summary(dataframe, numerical_col,plot):
    quantiles = [0.05,0.10,0.20,0.30,0.40,0.50,0.60,0.80]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)

for col in num_cols:
    num_summary(df,col,plot=True)

# Bonus
df = sns.load_dataset("titanic")
df.info()
for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)

cat_cols,num_cols,cat_but_car = grap_col_names(df)


### Hedef Değişken Analizi ###


pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)

def cat_summary(dataframe,col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_count(),
                        "Ratio": 100 * dataframe[col_name].value_counts()/len(dataframe)}))
    print("##################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

def grap_col_names(dataframe, cat_th=10,car_th=20):

    """   Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini döndürür.


Parameters  
-----------  
dataframe: dataframe  
    değişken isimleri alınmak istenen dataframe'dir.  
cat_th: int, float  
    numerik fakat kategorik olan değişkenler için sınıf eşik değeri  
car_th: int, float  
    kategorik fakat kardinal değişkenler için sınıf eşik değeri  

Returns  
-------  
cat_cols: list  
    Kategorik değişken listesi  

num_cols: list  
    Numerik değişken listesi  

cat_but_car: list  
    Kategorik görünümlü kardinal değişken listesi  """
    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object","bool"]]
    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int","float"]]
    cat_but_car = [col for col in df.columns if df[col].nunique()> 20 and str(df[col].dtypes) in ["category", "object"]]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]
    num_cols = [col for col in df.columns if df[col].dtypes in ["int","float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]
    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f"cat_cols: {len(cat_cols)}")
    print(f"Observations: {len(num_cols)}")
    print(f"Observations: {len(cat_but_car)}")
    print(f"Observations: {len(num_but_cat)}")

    return cat_cols,num_cols,cat_but_car

cat_cols, num_cols,cat_but_car = grap_col_names(df)
df.head()

df["survived"].value_counts()
cat_summary(df,"survived")


## HEDEF DEĞİŞKENİN KATEGORİK DEĞİŞKENLER İLE ANALİZİ ##

df.groupby("sex")["survived"].mean()

def target_summary_with_cat(dataframe, target,categorical_col):
    print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()}),end ="\n\n\n")

target_summary_with_cat(df,"survived","pclass")

for col in cat_cols:
    target_summary_with_cat(df,"survived",col)


## HEDEF DEĞİŞKENİN SAYISAL DEĞİŞKENLER İLE ANALİZİ ##

df.groupby("survived")["age"].mean()
df.groupby("survived").agg({"age":"mean"})

def target_summary_with_num(dataframe,target,numerical_col):
    print(dataframe.groupby(target).agg({numerical_col:"mean"}), end ="\n\n\n")

target_summary_with_num(df,"survived","age")  

for col in num_cols:
    target_summary_with_num(df,"survived",col)



### 5.KORELASYON ANALİZİ (Analysis of Correlation) ###

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_csv("data.csv")
df = df.iloc[:,1:-1]
df.head()

num_cols = [col for col in df.columns if df[col].dtype in [int,float]]
corr = df[num_cols].corr()

sns.set(rc={'figure.figsize':(12,12)})
sns.heatmap(corr,cmap="RdBu")
plt.show()

### YÜKSEK KORELASYONLU DEĞİŞKENERİN SİLİNMESİ ##

cor_matrix = df.corr().abs()

#        0         1         2         3
# 0  1.00000  0.117570  0.871754  0.817941
# 1  0.117570  1.00000  0.428440  0.366126
# 2  0.871754  0.428440  1.00000  0.962865
# 3  0.817941  0.366126  0.962865  1.00000

# #  0         1         2         3
# 0  NaN    0.11757   0.871754   0.817941
# 1  NaN       NaN    0.428440   0.366126
# 2  NaN       NaN         NaN   0.962865
# 3  NaN       NaN         NaN        NaN

upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool))
drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > 0.90)]
cor_matrix[drop_list]
df.drop(drop_list,axis=1)


def high_correlated_cols(dataframe, plot=False, corr_th=0.90):
    corr = dataframe.corr() # korelasyon oluşturduk
    cor_matrix = corr.abs() #mutlak değerini aldık
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k =1).astype(np.bool))
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > corr_th)]
    if plot:
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.set(rc={'figure.figsize': (15,15)})
        sns.heatmap(corr, cmap="RdBu")
        plt.show()
    return drop_list


high_correlated_cols(df)
drop_list = high_correlated_cols(df)
df.drop(drop_list, axis=1)
high_correlated_cols(df.drop(drop_list,axis=1),plot=True)