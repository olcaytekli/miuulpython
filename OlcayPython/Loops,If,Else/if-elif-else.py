# username = "sadikturan"
# password = "1234"

# # isLoggedin = (username == "sadikturan"): #and (password == "1234")  #if bloğunun yanındaki false bilgisi veriyorsa else'e geçeriz.
#                                                 #Kullanıcı şifrenin mi yoksa mailin mi yanlış olduğunu bilmek ister.


# if (username == "sadikturan"): 
#         if (password == "12345"):     
#             print("Hoş geldiniz")
#         else:
#             print("parola yanlış")

# else:
#     print("username yanlış")





# x = 20
# y = 20

# if x > y:
#     print("x y den büyük")
# elif x == y:                       #2.koşul olarak kullanılır.
#     print("x y eşit")
# else:
#     print("y x den büyük")


# x = int(input("x: "))   #çünkü sayı string olacak ve bizim ifdeki koşulumuz sayıyla alakalı
# y = int(input("y: "))

# if x > y:
#     print("x y den büyük")
# elif x == y:                       #2.koşul olarak kullanılır.
#     print("x y eşit")
# else:
#     print("y x den büyük")


num = int(input("sayı: "))

if num > 0:
    print("sayi pozitif")
elif num < 0:
    print("sayı negatif")
else:
    print("sayı sıfır")