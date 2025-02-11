#decorator fonksiyonları bir fonksiyona özellik eklemek istediğimiz zaman kullanıyoruz.

# def my_decorator(func):
#     def wrapper(name):
#         print("fonksiyondan önce işlemler")
#         func(name)
#         print("fonksiyondan sonraki işlemler")
#     return wrapper

# @my_decorator
# def sayHello(name):
#     print("hello",name)

# sayHello("ali")

import math
import time


def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)   
        func(*args,**kwargs)
        finish = time.time()
        print("fonksiyon " + func.__name__ +  str(finish-start) + " saniye sürdü.")
    return inner

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))

@calculate_time
def faktoriyel(num):
    start = time.time()
    time.sleep(1)

    print(math.factorial(num))

    finish = time.time()
    print("fonksiyon"+  str(finish-start) + " saniye sürdü.")
@calculate_time
def toplama(a,b):
    print(a+b)

usalma(2,3)
faktoriyel(4)
toplama(10,20)
