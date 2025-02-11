import numpy as np

# 1- (10,15,30,45,60) değerlerine sahip numpy dizisi oluşturunuz.
numbers = np.array([10,15,30,45,60])

# 2- (5-15) arasındaki sayılarla numpy dizisi oluşturunuz.
numbers = np.arange(5,15)

# 3- (50-100) arasında 5'er 5'er artarak numpy dizisi oluşturunuz.
numbers = np.arange(50,100,5)

# 4- 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz.
numbers = np.zeros(10)

# 5- 10 elemanlı birlerden oluşan bir dizi oluşturunuz.
numbers = np.ones(10)

# 6- (0-100) arasında eşit aralıklı 5 sayı üretin.
numbers = np.linspace(0,100,5)

# 7- (10-30) arasında rastgele 5 tane tam sayı üretin.
numbers = np.random.randint(10,30,5)

# 8- [-1 ile 1] arasında 10 adet sayı üretin.
numbers = np.random.randn(10)

# 9- (3x5) boyutlarında (10-50) arasında rastgele bir matris oluşturunuz.
numbers = np.random.randint(10,50,15)
numbers1 = numbers.reshape(3,5)
# print(numbers1)

# 10- Üretilen matrisin satır ve sütun sayıları toplamlarını hesaplayınız?
toplam = numbers1.sum(axis=0)
toplam1= numbers1.sum(axis=1)
# print(toplam)
# print(toplam1)

# 11- Üretilen matrisin en büyük, en küçük ve ortalaması nedir?
numbers2 = numbers1.max()
numbers2 = numbers1.max()
numbers2 = numbers1.mean()

# 12- Üretilen matrisin en büyük değerinin indeksi kaçtır?
numbers2 = numbers1.argmax()
# print(numbers2)
# 13- (10,20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.
numbers = np.arange(10,20)
result = numbers[:3]

# 14- Üretilen dizinin elemanlarını tersten yazdırın.
result = numbers[::-1]

# 15- Üretilen matrisin ilk satırını seçiniz.
result = numbers1[0]

# 16- Üretilen matrisin 2.satır 3.sütunundaki elemanı hangisidir?
result = numbers1[1,2]

# 17- Üretilen matrisin tüm satırlardaki ilk elemanı seçiniz.
result =numbers1[:,0]

# 18- Üretilen matrisin her bir elemanının karesini alınız.
result = numbers1 ** 2

# 19- Üretilen matris elemanlarının hangisi pozitif çift sayıdır?
#       Aralığı (-50, +50) arasında yapınız.

matris = np.random.randint(-50,+50,15).reshape(3,5)

ciftler = matris[matris % 2 == 0]

sayilar = ciftler[ciftler > 0]


print(sayilar)
# print(numbers1)
# print(result)
# print(numbers)