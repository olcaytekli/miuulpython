# RANGE METODU

# for item in range(10):          # 10'a kadar yaz diyoruz yani range bize bir liste oluşturuyor
#     print(item)

# for item in range(50,100,10):     # 50den başla 100e kadar 10 ar 10 ar arttır.
#     print(item)


# for item in range(50,100,20):     # 50den başla 100e kadar 10 ar 10 ar arttır.
#     print(item)

# print(list(range(5,100,10)))


# ENUMERATE METODU

# index = 0
# greeting = "Hello There"

# for letter in greeting:
#     print(f"index: {index} letter: {greeting[index]}")
#     index += 1

# index = 0
# greeting = "Hello"

# for index,letter in enumerate(greeting):
#     print(f"index: {index} letter: {letter}")


# ZIP METODU

#listeleri bir liste içine toplar

list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]
list3 = [100,200,300,400,500]

print (list(zip(list1,list2,list3)))

for item in zip(list1,list2,list3):
    print(item)

for a,b,c in zip(list1,list2,list3):
    print(a,b)