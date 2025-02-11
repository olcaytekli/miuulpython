# with open("newfile.txt","r",encoding ="utf-8") as file:
#     content = file.read()
#     print(content)
#     file.seek(10)
#     print(file.tell())
#     content2 = file.read()
#     print(content2)



########### UPDATING ###########
# with open("newfile.txt","r+",encoding="utf-8") as file:
#     file.seek(20)   #istediğimiz konumda güncelleme işlemi
#     file.write("deneme")


# with open("newfile.txt","r+",encoding="utf-8") as file:
#     print(file.read())

#### sayfa sonunda güncelleme
# with open("newfile.txt","a",encoding="utf-8") as file:
#     file.write("\nEmel Turan")

###sayfa başında güncelleme
# with open("newfile.txt","r+",encoding="utf-8") as file:
#     content = file.read()
#     content = "Oktay tekli\n" + content 
#     file.seek(0)
#     file.write(content)
#     print(content)

with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())


#### sayfa ortasında güncelleme
with open("newfile.txt","r+",encoding="utf-8") as file:
    list = file.readlines()
    list.insert(1,"Lale Tekli\n")
    file.seek(0)
    file.writelines(list)
with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())








