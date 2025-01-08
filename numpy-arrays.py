import numpy as np

# result = np.array([1,3,5,7,9])
# result = np.arange(1,10)  # 1 den 10a kadar 10 dahil olmayacak şekilde liste hazırlar.
# result = np.arange(10,100,3)    #10dan 100e kadar 3er 3er bir liste
# result = np.zeros(10)   # 10 tane sıfır hepsi float bir değer
# result = np.ones(10)    # 10 tane 1 hepsi float bir değer 
# result = np.linspace(0,100,5) # verdiğimiz başlangıç ve bitiş değerlerini 5 eşit parçaya böler
# result = np.linspace(0,5,5) # adım sayısı olarak 5 eşit parçaya bölüyor 1 1 1 değil 0. 1.25 vs
# result = np.random.randint(0,10)
# result = np.random.randint(20)  # 0 la 20 arasında bir sayı üretir 0 dahil ,20 değil
# result = np.random.randint(1,10,3)  # 1 ile 10 arasında 3 tane sayı üret
# result = np.random.rand(5)  # 0 ile 1 arasında 5 tane sayı üretmek için
# result = np.random.randn(5) # negatif değerler de katılır
# np_array = np.arange(50)
# np_multi = np_array.reshape(5,10) # 1 den 50ye kadar olan sayıları 5 e 10luk matris olarak hazırlar
# print(np_multi.sum(axis=1)) #matristeki satırların toplamı
# print(np_multi.sum(axis=0)) #sütunların toplamı

rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
result = rnd_numbers.max() # üretilen sayılar içerisindeki en büyük sayı
result = rnd_numbers.min()
result = rnd_numbers.mean() #üretilen sayıların ortalamasını verir
result = rnd_numbers.argmax()   #üretilen sayıların en büyüğünün index numarası
result = rnd_numbers.argmin()   #üretilen sayıların en küçüğünün index numarası

print(result)

