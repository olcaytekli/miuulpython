numbers = [1,10,5,16,4,9,10]
letters = ["a", "g", "s", "b", "y","a", "s"]

val = min(numbers)
val = max(numbers)
val = max(letters)
val = min(letters)

val = numbers[3:6]
val = numbers[:3]       #baştan itibaren 3 indexi alır.
val = numbers[4:]       #4.indexten başla sona doğru git.

numbers[4] = 40         # böyle yaparak 4.indexteki rakamı istediğim sayıyla değiştirebilirim mesela 40 gibi

numbers.append(49)      # append metotu ile 49 sayısı listenin sonuna eklenir

numbers.insert(3,78)    # insert metodu ile istediğimiz yere sayı ekleyebiliyoruz. örnekte 3.indexten sonra 78 eklendi.
numbers.insert(-1, 52)  #en sondakinden bir öncekine ekler.

# numbers.pop()         #en sondaki elemanı siler
# numbers.pop(0)          #en baştaki elemanı siler yani parantezin içi önemli.
# numbers.remove(49)        # 49 rakamını sildirdik.

# numbers.sort()              #liste sayısal büyüklüğe göre sıralanır.
# letters.sort()              #liste alfabetik sıralanır.    

# numbers.reverse()           #listeyi terstten yazar.
# letters.reverse()           #terstten yazar.





print(len(numbers))
print(len(letters))

print(numbers.count(10))
print(letters.count("a"))

# numbers.clear()         #bütün elemanları silmek için kullanılır.
print(numbers)