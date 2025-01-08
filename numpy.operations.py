import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

print(numbers1)
print(numbers2) 

result = numbers1 + numbers2  # iki dizinin aynı indeksteki elemanları toplayıp bundan yeni bir dizi çıkarır
result = numbers1 + 10  #her bir elemanın üstüne 10 değeri eklenir
result = numbers1 - numbers2    # iki dizinin farkı 
result = numbers1 - 10  #diziden 10 sayısı çıkarılır
result = numbers1 * numbers2    #iki dizinin elemanları çarpılır  [3465 3375 6141  280 2268 4680]
result = numbers1 * 10 
result = numbers1 / numbers2 
result = numbers1 / 10 

result = np.sin(numbers1)   # sinüsünü alır 
result = np.cos(numbers1)   # cosinüsünü alır 
result = np.sqrt(numbers1)  # her bir elemanın karekökünü alıp yeni bir dizi oluşturur
result = np.log(numbers1)

mnumbers1 = numbers1.reshape(2,3)
mnumbers2 = numbers2.reshape(2,3)

print(mnumbers1)
print(mnumbers2)

# result = np.vstack((mnumbers1,mnumbers2))   # matrisleri dikey olarak birleştirir
# result = np.hstack((mnumbers1,mnumbers2))   #matrisleri yatay olarak birleştirir

result = numbers1 >= 50  #numbers1 deki her elemana bakar ve bunların 5ten büyü kolup olmadığını kontrol eder ve tru veya false der
result = numbers1 % 2 == 0

print(numbers1[result]) # hangi değerlerin true değer verdiğini gösterdi


print(result)