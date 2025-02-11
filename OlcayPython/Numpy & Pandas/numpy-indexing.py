import numpy as np

numbers = np.array([0,5,10,15,20,25])

result = numbers[5]
result = numbers[-1]
result = numbers[0:3]   # ilk 3 eleman
result = numbers[:3]    # yine ilk 3 eleman
result = numbers[3:]    # 3.indexten başla sona kadar git
result = numbers[::]    # bütün liste
result = numbers[::-1]  # listeyi terstten yazar
result = numbers[::-2]  # sağdan sola doğru bir elemanı alır bir elemanı almaz

numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])   #karşımıza 3x3lük bir matris gelir
result = numbers2[0]
result = numbers2[2]
result = numbers2[0,2]  # 0.indeksin 2.indeksi (1.satırın 3.elemanı)
result = numbers2[2,1]  # 2.indeksin 1.indeksi (3.satırın 2.elemanı)
result = numbers2[:,2]  # bütün satırlardan 3.elemanı yani 2.indeksi al [10 25 85]
result = numbers2[:,0]  #[0,15,50]
result = numbers2[:,0:2]    #bütün satırları seç ve bu satırlardan 0dan 2.indekse kadar olanları getir.
result = numbers2[-1,:]     # -1.satırın bütün kolonlarını al [50,75,85]
result = numbers2[:3,:3]    #bütün sütunlardaki bütün kolonları al 
result = numbers2[:2,:2]    # 0 ve 1 indeks içindeki 0 ve 1 kolonlarını al

# print(result)

arr1 = np.arange(0,10)
# arr2 = arr1  #referans kopyalaması
arr2 = arr1.copy() #bu şekilde yaparsak her ikisin farklı adreslere kopyalarız ve bu şekilde birinde yapılan değişiklik öbürünü etkilemez olacak


arr2[0] = 20

print(arr1)    #arr1 ve arr2 üzerindeki yapacağımız değişiklik ikisini de etkiler çünkü aynı adresteler
print(arr2)
