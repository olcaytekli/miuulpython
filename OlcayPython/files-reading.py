# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi, dosya_erisme_modu)
# dosya_erisme_modu => Dosyayı hangi amaçla açtığımızı belirtir.

# Dosya Erişim Modları:
# "w" (Write): Yazma modu. 
#       ***Dosyayı konumda oluşturur.
#       ***Dosya içeriğini siler ve yeniden ekleme yapar.

# file = open("newfile.txt","w")
# file.close()

# file = open("C:/users/olcay/desktop/newfile.txt","w")   #dosya oluşturduk

# file = open("newfile.txt","w",encoding="utf-8")
# # file.write("SadıkTuran")
# file.close()

# "a" (Append): Ekleme modu. Dosya konumda yoksa oluşturur.
# file = open("newfile.txt","a",encoding="utf-8")
# file.write("\nÇınar Turan")
# file.close()


# "x" (Create): Oluşturma modu. Dosya zaten varsa hata verir.
# file = open("newfile.txt","x",encoding="utf-8")



# "r" (Read): Okuma modu. Varsayılan moddur. Dosya konumda yoksa hata verir.
# try:
#     file = open("newfile2.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("Dosya okuma hatası")
# finally:
#     print("Dosya kapandı.")
#     file.close()

# # print(file)

file = open("newfile.txt","r",encoding="utf-8")

#for döngüsü

# for i in file:
#     print(i, end="")

#read() fonksiyonu

# content1 = file.read()
# print("içerik 1")
# print(content1)

# file = open("newfile.txt","r",encoding="utf-8")
# content2 = file.read()

# print("içerik 2")
# print(content2)

# content = file.read(5)
# print(content)

# ****** readline() fonksiyonu

# file = open("newfile.txt","r",encoding="utf-8")
# content = file.readline()
# content = file.readline()   #bir satır okur

# print(content)



# ********** readlines() fonksiyonu
liste = file.readlines()
print(liste)


file.close()