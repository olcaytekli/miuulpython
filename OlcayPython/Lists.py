#String bir karakter dizisidir ve bunun içindeki her bir karakter aslında bir listenin bir öğesini temsil eder.

# my_list = [1,2,3]
# print(my_list)

message = "Hello There. My name is Olcay Tekli".split() #split yazmazsak bize harf verir fakat splitle beraber ayırdığımız için direkt kelimeyi verir.

list1 = ["one","two","three"]
list2 = ["four","five","six"]

numbers = list1 + list2    #string işlem gibi toplar
print(numbers)  
print(len(numbers))
print(message[1])


userA = ["Olcay", 24]
userB = ["Oktay",25]
users = userA + userB

print(userA)
print(userB)
print(users)

#List içine bir liste elemanı yazmak.
userA = ["Olcay", 24]
userB = ["Oktay",25]
users = [userA, userB]

print(userA)
print(userB)
print(users)    

a = users[1]

print(users[1])   #Listenin içindeki 1.elemana ulaşmak istersek.
print(a[0])    #users1 in içindeki 0.elemana ulaşmak istersek.
print(users[0][1])   #0.listenin 1.elemanı
