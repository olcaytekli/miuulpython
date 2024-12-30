# # liste = [1,2,3,4,5]

# # iterator = iter(liste)

# # print(next(iterator))  #iteratorü her next elemanı ile çağırdığımız zaman listeden bir elemanı getirir
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))

# # for i in liste:
# #     print(i)

# ### for döngüsünün arkasındaki işlem ##
# liste = [1,2,3,4,5]
# iterator = iter(liste)

# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break

# class MyNumbers:
#     def __init__(self,start,stop):
#         self.start = start
#         self.stop = stop

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.start <= self.stop:
#             x = self.start
#             self.start += 1
#             return x 
#         else:
#             raise StopIteration
        
# list = MyNumbers(10,40)
# myiter = iter(list)
# # print(next(myiter))
# # print(next(myiter))

# while True:
#     try:
#         element = next(myiter)
#         print(element)
#     except StopIteration:
#         break

# print(next(myiter))
# print(next(myiter))


# for x in list:
#     print(x)



############# GENERATORS ##########

# generators bellekte yer işgal etmeyen bir iterator üretiyor.

# def cube():
#     for i in range (5):
#         yield i ** 3

# for i in cube():
#     print(generator)

generator = (i**3 for i in range(5))
print(generator)

for i in generator:
    print(i)

# print(next(generator))
# print(next(generator))
# print(next(generator))


