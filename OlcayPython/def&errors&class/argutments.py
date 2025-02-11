# def changeName(n):   #gönderdiğimiz parametreyi ad olarak değiştirelim.
#     n = "ada"

# name = "yiğit"
# changeName(name)
# print(name)


# def change(n):
#     n[0] = "istanbul"

# sehirler = ["ankara","izmir"]
# change(sehirler[:])
# print(sehirler)



# sehirler = ["ankara","izmir"]
# n = sehirler[:]   #slicing

# n[0] = "istanbul"
# print(sehirler)
# print(n)



# def add(a, b, c = 0):  # en az en fazla 5 parametre. 6 yollamak istediğimizde

# def add(*params):
#     print(params)   #eklediğimiz parametreleri bir liste şeklinde gösterir.
#     return sum((params)) 

# print(add(10,20))
# print(add(10, 20 ,30))
# print(add(10, 20 ,30,40,80))

# yukarıdaki örnek için sum kullanmak istemezsek

# def add(*params):
#     sum = 0
#     for n in params:
#         sum = sum + n

#     return sum

# print(add(10,20))
# print(add(10, 20 ,30))
# print(add(10, 20 ,30,40,80))

def displayUser(**args):  #bir dictionary geleceğini bildirmek için iki yıldız attık.
    print(type(args))
    for key, value in args.items():
        print("{} is {}".format(key, value))

displayUser(name = "Çınar", age = 2, city = "İstanbul")
displayUser(name = "Ada", age = 12, city = "Kocaeli", phone = "123456")
displayUser(name = "Yiğit", age = 14, city = "Ankara", phone = "456789")


## Bir liste ve dicti. beraber kullanmak istiyorsak.

def myFunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,key1="value1",key2 = "value2")




