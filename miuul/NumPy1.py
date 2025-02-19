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

