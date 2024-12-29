# # def square(num): return num ** 2

# numbers = [1,3,5,9]

# result = list(map(lambda num: num** 2,numbers))


# # for item in map(square, numbers):
# #     print(item) 
# print(result)


# # square = lambda num: num **2
# # numbers = [1,3,5,9]

# # result = list(map(square,numbers))
# # result = square(3)
# # print(result)


# square = [1,3,5,9,10]

# def check_even(num): return num % 2 == 0
# check_even = lambda num: num % 2 == 0
# # result = list(filter(check_even, numbers))
# # result = list(filter(lambda num: num % 2 == 0, numbers))

# result = check_even(numbers[2])


# print(result)



###############SCOPE##################
# x = "global x"

# def function():
#     x="local x"

# function()
# print(x)


#global olarak tanımlanan name değeri
name = "Çınar"

def changeName(new_name):
    #local olarak tanımlanmış name değeri.
    name = new_name
    print(name)

changeName("Ada")
print(name)
########
name = "global string"
def greeting():
    # name = "Çınar"

    def hello():
        # name = "Ada"
        print("hello " + name)
    hello()

greeting() 
#############

x = 50
def test():
    global x
    print (f"x : {x}")
    
    x=100
    print(f"changed x to {x}")

test()
print(x)

