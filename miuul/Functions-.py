#### Fonksiyonlar ####

print("a" , "b", sep = "__")  #a ve b arasına __ koyar


### Fonksiyon Tanımlama ###

def calculate(x):   #fonksiyona bir ad verdik daha sonra bu fonk. kullanacağımız bir argüman varsa onu girdik
    print (x*2)   #bu kısım fonksiyonun gövdesi ve yapılacak işi gösterir

calculate(5)    #fonksiyonu çağırıyoruz


##### İki argümanlı/parametreli bir fonksiyon tanımlayalım. #####

def summer(arg1,arg2):
    print(arg1 + arg2)

summer(7,8)

### Docstring ###   (fonksiyonlarımıza herkesin anlayabileceği şekilde bilgi notu girilmesi)

def summer(arg1,arg2):

    """
    Sum of two numbers

    Parameters/Args
    ----
        arg1: int,float

        arg2: int,float

    Returns:
        int , float
    -----
    """

    print(arg1 + arg2)

summer(1,3)


### Fonksiyonların Statement/Body Bölümü
##      Statements (function body)

def say_hi(string):   #bir fonksiyonu argümansız da çalıştırabiliriz fakat argüman belirtiyorsak,çalıştırırken bir argüman girmek zorundayız
    print(string)
    print("Hi")
    print("Hello")

say_hi("miuul")

def multiplication(a,b):
    c = a* b
    print(c)

multiplication(10,9)


# girilen değeleri bir liste içinde saklayacak fonksiyon.

list_store = []

def add_element(a,b):
    c = a* b
    list_store.append(c)
    print(list_store)

add_element(1,8)
add_element(10,8)

##### Ön Tanımlı Argümanlar/Parametreler (Default Parameters/Arguments)

def divide (a,b):
    print(a/b)

divide(1,2)

def divide (a,b=1):   #b eşittir 1 diyerek önceden onu tanımlıyoruz yani istersek onu çalıştırırken b değeri girmeyebiliriz
    print(a/b)

divide(1)


#### Ne Zaman Fonksiyon Yazma İhtiyacımız Olur? ####

#       DONT REPEAT YOURSELF!!!

#       Birbirini tekrarlayan durumlarda fonksiyon yazarız.  


#### Return: Fonksiyon Çıktılarını Girdi Olarak Kullanmak
#bir fonk çıktısını kullanmak istiyorsak return
def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture *2 
    charge = charge * 2
    output = (varm + moisture) / charge

    return varm, moisture, charge, output

varm, moisture, charge, output = calculate(98,12,78)


### Fonksiyon İçerisinden Fonksiyon Çağırmak

def calculate(varm, moisture, charge):
    return int((varm + moisture) / charge)

calculate(90,12,12) * 10

def standardization(a , p):
    return a * 10 / 100 * p * p

standardization(45,1)

def all_calcutalion(varm,moisture,charge,p):
    a = calculate(varm, moisture,charge)
    b = standardization(a , p)
    print(b * 10)

all_calcutalion(1,3,5,12)

def all_calcutalion(varm,moisture,charge,a,p):
    print(calculate(varm, moisture,charge))
    b = standardization(a , p)
    print(b * 10)

all_calcutalion(1,3,5,19,12)


### Lokal & Global Değişkenler (Locak & Golbal Variables)

list_store =  [1 , 2]   #global

def add_element(a,b):
    c = a* b  #c bu fonksiyonun local değişkenidir
    list_store.append(c)
    print(list_store)

add_element(1,9)
