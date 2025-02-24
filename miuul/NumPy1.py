import numpy as np 

## Numpysız sadece python yoluyla işlem yapma

a = [1,2,3,4]
b = [2,3,4,5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])
print(ab)

## numpy ile

a = np.array([1,2,3,4])
b = np.array([2,3,4,5])

print(a*b)

# NumPy Array'i Oluşturmak (Creating Numpy Arrays) # 

import numpy as np 

np.array([1,2,3,4,5])

np.zeros(10, dtype =int)
np.random.randint(0 ,10, size = 10)

# NumPy Array Özellikleri (Attributes of Numpy Arrays)

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10, size = 5)
print(a)
print(a.ndim)  #1
print(a.shape)  #(5,)
print(a.size)   #5
print(a.dtype)  #int32

# Yeniden Şekillendirme (Reshaping)

np.random.randint(1, 10 , size = 9)
ar = np.random.randint(1, 10 , size = 9).reshape(3,3)
print(ar)


#Index Seçimi (Index Selection)

import numpy as np
a = np.random.randint(10, size=10)
a[0] 
a[0:5]
a[0] = 99  #0.indeksi değiştirme

m = np.random.randint(10 , size = (3,5))
m[0,0]
m[1,1]
print(m)


#Fancy Index
v = np.arange(0 , 30 , 3)

v[1]
v[4]

catch = [1,2,3]

v[catch]


## Numpy Koşullu İşlemler (Conditions on Numpy) ##

v = np.array([1,2,3,4,5])

# Klasik Döngü ile

ab = []
for i in v:
    if i < 3:
        ab.append(i)
print(ab)

#Numpy ile 
v < 3

v[v < 3]

###Matematiksel İşlemler (Mathematical Operations) ###

v = np.array([1,2,3,4,5])

v / 5
v * 5 / 10
v ** 2
v - 1

np.subtract(v,1)  #her elemandan 1 çıkarır
np.add(v,1) #her elemana 1 ekler
np.mean(v)  # ortalamasını hesaplar
np.sum(v)   #tüm elemanları toplar
np.min(v)   #en küçük elemanı getirir
np.max(v)   #en büyük elemanı getirir
np.var(v)   #varyansını hesaplar

#Numpy ile İki Bilinmeyenli Denklem Çözümü#

# 5 * x0 + x1 = 12
# x0 + 3 * x1 = 10

a = np.array([[5,1],[1,3]])
b = np.array([12,10])

np.linalg.solve(a,b)