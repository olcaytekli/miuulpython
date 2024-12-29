"""
x = input ('1 sayı:')
y = input ('2.sayı:')



print (type(x))
print (type(y))

toplam = int (x) + int (y)

print(toplam)
"""

x = 5     #int
y = 2.5   #float
name = "Olcay"  #string
isOnline = True   #bool

# print(type(x))
# print(type(y))
# print(type(name))
# print(type(isOnline))

#Type Conversion

#int to float

# x = float (x)
# print(x)
# print(type(x))

# y = int(y)
# print(y)
# print(type(y))

# result = str (x) + str (y)
# print (result)
# print(type(result))

# isOnline = str (isOnline)
# print (isOnline)
# print(type(isOnline))

#bool dan int'e çevirme

isOnline = int(isOnline)
print(isOnline)
print (type(isOnline))     #true'nun int'e çevrilmiş hali 1'e denk geliyormuş



#tpye conversion demo

"""
Daire alanı: π r²
Dairenin çevresi: 2πr

Yarı çapı verilen bir dairenin alanı ve çevresini hesaplayınız. 
"""

pi = 3.14
r = float (input("yarı çap:"))

alan = r * r * pi 
cevre = 2 * pi * r 

# print("alan: ", alan)
# print("cevre: ", cevre)

# print("alan: ", alan, "cevre: ", cevre)
print("alan" +str (alan), "cevre: "+ str(cevre))    #BU ÜÇ FORMDAN BİRİ OLUR
