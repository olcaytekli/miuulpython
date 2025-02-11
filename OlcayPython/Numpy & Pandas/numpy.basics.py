import numpy as np

#python list
py_list = [1,2,3,4,5,6,7,8,9]

#numpy array   #numpy üzerinden bir dizi oluşturma ve bu diziye de array denir.

np_array = np.array([1,2,3,4,5,6,7,8,9])

print(type(py_list))    # tipi list
print(type(np_array))   # tipi ndarray

#çok boyutlu bir dizi oluşturmak istersek

py_multi = ([1,2,3],[4,5,6],[7,8,9])  #çok boyutlu bir liste
np_multi = np_array.reshape(3,3)   #bu şekilde çok boyutlu bir dizi oluşturabiliriz. Buna 3 x 3 matris de denir.

print(py_list)
print(np_multi)

#numpy objelerinin boyutlarına bakmak için

print(np_array.ndim)   # 1 boyutlu
print(np_multi.ndim)   # 2 boyutlu

# shape lerine bakarsak

print(np_array.shape)   # (9,)
print(np_multi.shape)   # (3,3)

