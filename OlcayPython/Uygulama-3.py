website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

# 1.Soru " Hello World " karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
# message = " Hello World "
# message = message.strip()
# print(message)

                       #hocanın yaptığı
# message = " Hello World ".strip()   #soldan silmek istersek lstrip sağdan rstrip
# print(message)

message = website.lstrip("htp:/")    #website mesajında sadece www.sadikturan.com kalmasını istiyorsak
print(message)

# 2.soru "www.sadikturan.com" içindeki sadikturan bilgisi haricindeki her karakteri silin.

message = "www.sadikturan.com".strip("w.moc")
print(message)

# 3.Soru "course" karakter dizisinin tüm karakterlerini küçük harf yapın.

message = course.lower()
print(message)

# 4.Soru "website" içinde kaç tane a karakteri vardır? (count("a"))

message = website.count("a")
print(message) 

# message = website.count("www",0,10)    #www yu 0 ve 10 arasında arıyor ve kaç tane olduğunu söylüyor.

# 5.Soru "website"  "www" ile başlayıp "com" ile bitiyor mu?

message = website.startswith("www") 
print(message)

# 6.Soru "website" içinde ".com" ifadesi var mı?

message = website.find(".com")   #buldu ve indexini söyledi
# # message = website.find(".com",0,10)  # 0 ve 10 aralığını kontrol etti.
print(message)

# message = course.rfind("Python")
# print(message)
# message = website.index("com")
 #print(message)

 # 7.Soru "course" içindeki karakterlerin hepsi alfabetik mi? (isalpha(alfabetik mi),isdigit(rakam mı))

message = course.isalpha()   #False dedi çünkü sayılar da var.
print(message)

message = "Hello".isalpha()
print(message)

# 8.Soru "Contents" ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

message = "Contents".center(50,"*")
# message = "Contents".ljust(50, "*")     sadece soluna 50 boşluk ekler ve yıldızlar.
print(message)

# 9.Soru  "Course" karakter dizisindeki tüm boşluk karakterlerini "-" ile değiştirin.

message = course.replace(" ", "-")    # (" ", "-", 5) yazarsak sadece 5ine yapar.
print(message)

#10. Soru "Hello World" karakter dizisinin "World" ifadesini "There" olarak değiştirin.

message = "Hello World".replace("World","There")
print(message)

# 11.Soru  "course" karakter dizisinin boşluk karakterlerinden ayırın.

message = course.split(" ")
print(message)
