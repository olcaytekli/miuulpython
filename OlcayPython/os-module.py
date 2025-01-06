import os   #os modulü işletim sistemiyle alakalı bilgi sunar


result = os.name  #işletim sistemimin ismini verir

#etkin dizin öğrenme
# result = os.getcwd() #kullandığımız dosya hakkında bilgi verir

# dizin değiştirme
# osçchdir("C:\\")
# os.chdir("../..")

#klasör oluşturma
# os.mkdir("Yeni dosya")  #yaptığım zaman aynı dizinin içerisine yeni bir dosya oluşturur
# os.rename("yenidosya","yeniklasör") #istediğimiz klasörün ismini değiştirme
# os.rmdir("yenidosya")   #klasör silme

#listeleme
# result= os.listdir()
# result = os.listdir("C:\\")   #istediğimiz bir yerdeki listeleri listeleme

# for dosya in os.listdir():  #sadece py uzantılı dosyaları listelemiş oluruz
#     if dosya.endswith(".py"):
#         print(dosya)

import datetime
# result = os.stat("Lists.py")
#result =datetime.datetime.fromtimes.stamp(result.st_ctime) #oluşturulma tarihi
#result = datetime.datetime.fromtimestamp(result.st_atime) #son erişilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime) #değiştirilme tarihi

os.system("notepad.exe")   #istediğimi dosyayı çalıştırma


print(result)

