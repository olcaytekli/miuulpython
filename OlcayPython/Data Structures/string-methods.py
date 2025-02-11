message = "Hello There. My name is Olcay Tekli"

#message = message.upper()  #upper metodu bütün karakterleri büyük harfle yazar.
#message = message.lower()   #lower metodu bütün karakterleri küçük harfle yazar.
#print(message[2])     sayı vererek istediğimiz kelimeyi alırız.

#message = message.title()   #title metodu kelimelerin baş harfini büyük yazar.
#message = message.capitalize()  #verilen string ifadenin yalnızca baştaki kelimesinin baş harfi büyük olur.
#message = message.strip() #oldu ki boşlukla yazdı strip metoduyla bu boşluğu sileriz.
#message = message.split()  #cümleyi parçalarına ayırır.
#message = message.split(".")  #cümleyi noktadan noktaya ayır.
# message = message.split()
# message = " * ".join(message) #ayırdığımız kelimeleri tekrar birleştirebiliriz.


#index = message.find("Olcay")  #mesaj (. =üzerinden)  Olcay kelimesini bul ve bana hangi indexe karşılık geldiğini söyle.
#print(index)

# isFound = message.startswith("H") #isfound bulundu mu? mesaj H ile mi başlar?
# print(isFound)    #H ile başlıyorsa True yanıtı çıkar.

# isFound = message.endswith("H")     #mesaj H ile bitiyor mu?
# print(isFound)        #Bitmiyorsa False cevabı çıkar.

# message = message.replace("Olcay" , "Oktay")       #Olcay gördüğün yerleri Oktay'la değiştir.
# message = message.replace("ç","c").replace("ö","o").replace("ı","i")  #gibi gibi bunları çeşitlendirebiliriz

#message = message.center(50)     #50(fark etmez 100 de olur) satırlık bir boşluğun ortasına mesajımı yazmak için yani ortalamak için.
message = message.center(50, "*")    #Sağdan ve soldan olan 25 boşluğa yıldız koyar.

print(message)