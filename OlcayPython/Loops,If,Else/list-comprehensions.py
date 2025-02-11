numbers = []
for x in range(10):
    numbers.append(x)
print(numbers)



numbers = [x for x in range (10)]   #10 a kadar sayıları x e gönder.
print(numbers)




for x in range(10):
    print(x**2)
numbers = [x**2 for x in range(10)]
print(numbers)


numbers = [x*x for x in range(10) if x%3==0]   # 1 le 10 arasındaki 3e tam bölünenlerin karesini numbers listesine koy.
print(numbers)


myString = "Hello"
myList = []

for letter in myString:
    myList.append(letter)
print(myList)

myList = [letter for letter in myString]     #yukarıdakiyle aynı sonucu verir.
print(myList)


years = [1983,1999,2008,1956,1986]
ages = [2019-year for year in years]
print(ages)


results =[x if x%2==0 else "TEK" for x in range(1, 10)]   #işlem sağdan sola gidiyor yani ilk 1 ve 10 arası xleri sonra bu x eğer 2 ye tam bölünüyorsa bunu x olarak al listele.
print(results)


result = []
for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)   #ilk olarak x e 0 gelecek sonra y 0 1 2 yazdıracak bunu ekleyecek sonra x e 1 gelecek y ye tekrar 0 1 2 yazdıracak böyle böyle liste oluşacak.

numbers = [(x,y) for x in range(3) for y in range(3)]
print(numbers)        #yukarıdakinin aynısı

numbers = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(numbers)