#error => hata

# print(a) => NameError
# int("1a2") => ValueError
# print(10/0) => ZeroDivisionError    # 0 a bölünemez hatası
# print("denem"e) => SyntaxError    # yazım yanlışı hatası



#error handling => hata yönetimi 

# 0 girdiğimizde zerodivision hatası çıkacak bunun için önlem alacağız
# Hataya sebep olabilecekler işlemleri try ile engelleyeceğiz.

# try:
#     x = int(input("x:"))
#     y = int(input("y:"))   # 0 yerine bir harf girersek a vs. ValueError hatası verir bunu da engellemiliyiz.

#     print(x/y)
# except ZeroDivisionError:
#     print("y yerine 0 girilemez.")
# except ValueError:
#     print("x ve y için sayısal bir veri girmelisiniz.")

# except (ZeroDivisionError,ValueError) as e:     # hangi bilgiden dolayı hata verdiğini söyler.
#     print("yanlış bilgi girdiniz")
#     print(e)   #e yi yazmadan direkt yanlış bilgi girdiniz de yazdırabiliriz.

while True:   #Yanlış bilgi girdiğinde tekrardan sorar, girilmediyse break yapıp döngüyü bitirir.
    try:
        x = int(input("x:"))
        y = int(input("y:")) 

        print(x/y)

    except Exception as ex:
        print("yanlış bilgi girdiniz",ex)
        
    else:
        break
    finally:
        print("try except sonlandı")