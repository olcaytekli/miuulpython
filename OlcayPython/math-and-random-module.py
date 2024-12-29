# Yöntem 1
#import math
# import math as islem

# # value = dir(math)
# # value = help(math)
# #value = help(math.factorial)
# # value = math.sqrt(49)
# # value = math.factorial(5)
# # value = math.floor(5.9)
# # value = math.ceil(5.9)
# value = islem.factorial(5)

# Yöntem 2 
# from math import *

from math import factorial,sqrt,ceil
def sqrt(x):
    print("x:"+str(x))                  #hangisi altta olursa o ezer şu an fonksiyon altta
# value = factorial(5)
value = sqrt(9)
# value = ceil(9.8)
print(value)


###################### RANDOM MODULÜ #####################

import random 
# result = dir(random)
# result = help(random)

result = random.random()  #0.0 - 1.0 arası
result = random.random() * 100  # 0 ile 1 arasında ama sonradan 100le çarpıyor
result = int(random.uniform(1,10))
result = random.randint(1,100)

greeting = "hello there"

names = ["ali","yağmur","deniz","cenk"]
# result = names[random.randint(0,len(names)-1)]
result = random.choice(names)   #listenin içinden rastgele elemanı bizim için seçiyor
result = random.choice(greeting)

liste = list(range(10))
random.shuffle(liste)    # liste üzerindeki elemanların yerini rastgele değiştirir
result = liste

liste = range(100)
result = random.sample(liste,3)      #belirttiğimiz listeden istediğimiz kadar eleman çekiyor.
result = random.sample(names,2)
print(result)