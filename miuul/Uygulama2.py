# Uygulama - Mülakat Sorusu #

# Amaç: Çift sayıların karesi alınarak bir sözlüğe eklenmek istenmektedir.
# Key'ler orijinal değerler value'lar ise değiştirilmiş değerler olacak.

numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2

{n: n ** 2 for n in numbers if n % 2 == 0}


## List & Dict Comprehension Uygulamalar ##

# 1 - Bir Veri Setindeki Değişken İsimlerini Değiştirmek#

# before:
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

# after:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']

import seaborn as sns 

df = sns.load_dataset("car_crashes")

df.columns

for col in df.columns:
    print(col.upper())

A = []

for col in df.columns:
    A.append(col.upper())

df.columns = A

## list comp. ile yapmak

df.columns = [col.upper() for col in df.columns]


# 2 - İsminde "INS" olan değişkenlerin başına FLAG diğerlerine NO_FLAG eklemek istiyoruz.


car_crashes= ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

[col for col in df.columns if "INS" in col]

["FLAG_"+ col for col in df.columns if "INS" in col]

["FLAG_"+ col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

df.columns=["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]


# 3 - Amaç key'i string, value'su aşağıdaki gibi bir liste olan sözlük oluşturmak.
# Sadece sayısal değişkenler için yapmak istiyoruz.


# Output:
# {'total': ['mean', 'min', 'max', 'var'],
#  'speeding': ['mean', 'min', 'max', 'var'],
#  'alcohol': ['mean', 'min', 'max', 'var'],
#  'not_distracted': ['mean', 'min', 'max', 'var'],
#  'no_previous': ['mean', 'min', 'max', 'var'],
#  'ins_premium': ['mean', 'min', 'max', 'var'],
#  'ins_losses': ['mean', 'min', 'max', 'var']}

import seaborn as sns

df = sns.load_dataset("car_crashers")
df.columns

num_cols = [col for col in df.columns if df[col].dtype != "0"]
soz = {}
agg_list = ["mean","min","max","sum"]

for col in num_cols:
    soz[col] = agg_list

#kısa yol
new_dict = {col: agg_list for col in num_cols}

df[num_cols].head()

df[num_cols].agg(new_dict)