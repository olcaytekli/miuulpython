x = 10

# if x>5:
#     raise Exception("X, 5'ten büyük değer alamaz.")

# def check_password(pws):
#     import re
#     if len(pws) < 8:
#         raise Exception("Parola en az 7 karakter olmalıdır.")
#     elif not re.search("[a-z]",pws):
#         raise Exception("parola küçük harf içermelidir.")
#     elif not re.search("[A-Z]",pws):
#         raise Exception("parola büyük harf içermelidir.")
#     elif not re.search("[0-9]",pws):
#         raise Exception("parola rakam içermelidir.")
#     elif re.search("\s",pws):
#         raise Exception ("parola boşluk karakteri içermemelidir.")
#     else:
#         print("Geçerli parola")
    
# password = "aB12345678"

# try:
#     check_password(password)

# except Exception as ex:
#     print(ex)
# else:
#     print("Geçerli parola")
# finally:
#     print("validation tamamlandı.")


class Person:
    def __init__(self,name,year):
        if len(name) > 10:
            raise Exception("name alanı fazla karakter içeriyor.")
        else:
            self.name = name
p = Person("Aliiiiiiiiiiiii", 1989)
