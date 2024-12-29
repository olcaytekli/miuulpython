# # def sayHello(name = "user"):
# #     print("Hello" + name)

# # sayHello("Çınar")
# # sayHello("Ada")


# def sayHello(name = "user"):
#     return ("Hello" + name)

# msg = sayHello("Çınar")
# print(msg)


# def total(num1, num2):    #gönderdiğimiz iki sayıyı toplayan bir fonk. tanımladık
#     return num1 + num2

# result = total (10,20)
# print(result)

# def yasHesapla(dogumYili):
#     return 2019 - dogumYili

# ageCinar = yasHesapla(2017)
# print(ageCinar)


# def EmekliligeKacYilKaldi(dogumYili, isim):
#     """
#     DOCSTRING : Doğum yılınıza göre emekliliğinize kaç yıl kaldı.
#     INPUT: Doğum yılı
#     OUTPUT: Hesaplanan yıl bilgisi
#     """
#     yas = yasHesapla(dogumYili)
#     emeklilik = 65 - yas

#     if emeklilik > 0:
#         print(f"emekliliğinize {emeklilik} yıl kaldı")
#     else:
#         print("Zaten emekli oldunuz")

# EmekliligeKacYilKaldi(1983, "Ali")
# EmekliligeKacYilKaldi(1974, "Sude")

# print(help(EmekliligeKacYilKaldi))