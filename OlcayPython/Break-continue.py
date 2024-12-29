# name = "Sadik turan"

# for letter in name:
#     if letter == "a":
#         break   # a ya geldiği anda durdurur
#     print(letter)


# for letter in name:
#     if letter == "a":
#         continue   # a yı es geçer ve devam eder.
#     print(letter)

# break : istenen koşul sağlanınca direkt döngüyü bitirir.
# continue : istene koşul sağlandığında onu es geçip döngüyü devam ettirir
# x = 0

# # while x < 5:
# #     if x == 2:
# #         break
# #     print(x)
# #     x +=1

# # while x < 5:
# #     if x == 2:
# #         continue
# #     print(x)
# #     x +=1

# # Continue true işlemini iptal ettiği için tekrar başa döndürür ve x+=1 işlemi de continue yu
# #geçip işleneceği için devam edemez ve sürekli başa dönüo 0 ve 1 yazdırır.

# while x < 5: 
#     x +=1
#     if x == 2:
#         continue

#     print(x)


# Örnek 1-100 e kadar tek sayıların toplamı

x = 1
result = 0
while x <= 100:
    x += 1
    if x % 2 == 1:
        continue
    result += x

print(f"Toplam : {result}")


   