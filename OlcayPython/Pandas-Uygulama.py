import pandas as pd
import numpy as np

df = pd.read_csv("imdb_data.csv")

# 1- Dosyada hakkındaki bilgileri.
result = df
result = df.columns
result = df.info 

# 2- İlk 5 kaydı gösterin.
result = df.head()
# 3- İlk 10 kaydı gösterin
result = df.head(10)
# 4- Son 5 kaydı gösterin
result = df.tail()
# 5- Son 10 kaydı gösterin.
result = df.tail(10)
# 6- Sadece Movie_Name kolonunu alın.
result = df["movie_name"]
# 7- Sadece Movie_name kolonunu içeren ilk 5 kaydı alın.
result = df["movie_name"].head()
# 8- Sadece Movie_name ve Rating kolonunu içeren ilk 5 kaydı alın.
result = df[["movie_name","rating"]].head()
# 9- Sadece Movie_name ve Rating kolonunu içeren son 7 kaydı alın.
result = df[["movie_name","rating"]].tail(7)
# 10- Sadece Movie_name ve Rating kolonunu içeren ikinci 5 kaydı alın.
result = df[6:12][["movie_name","rating"]].head()
# 11- Sadece Movie_name ve Rating kolonunu içeren ve imdb puanı 8.0
# ve üstünde olan kayıtlardan ilk 50 tanesini alınız.
result = df[df["rating"]> 8.0][["movie_name","rating"]].head(50)
# 12- Yayın tarihi 2014 ile 2015 arasında olan filmlerin isimlerini getiriniz.
result = df[(df["movie_year"] >= 2014) & (df["movie_year"] <= 2015 )][["movie_name","movie_year"]]

#BEN DE BU SORU YOK AMA CEVABI

# result = df[(df["Num_Reviews"] > 100000) | ((df["Rating"] >= 8 & df["Rating"] <=9))]["movie_title","number_reviews"]

print(result)
