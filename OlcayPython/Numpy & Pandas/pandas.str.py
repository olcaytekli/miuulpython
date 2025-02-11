import pandas as pd

data = pd.read_csv("imdb_data.csv")

data.dropna(inplace = True) #NaN olan yerler gitti

# data["movie_name"] = data["movie_name"].str.upper()  #movie name içinde olanları büyük harfle yazdırdı
# data["movie_name"] = data["movie_name"].str.lower()  #hepsini bu sefer küçük harf yapar
# data["index"] = data["movie_name"].str.find("a")
# data = data.genre.str.contains("Drama")     #genre içinde drama barındıranları true olarak getirir
# data = data.movie_name.str.replace(" ","-")     #movie namedeki boşluk karakterlerini - ile değiştir
data[["FirstName","LastName"]] = data["director_name"].loc[data["director_name"].str.split().str.len()==2].str.split(expand=True) #firsname ve last name diyei ki kolon oluşturuldu



print(data.head())