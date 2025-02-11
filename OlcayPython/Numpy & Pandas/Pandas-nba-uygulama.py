import pandas as pd

df = pd.read_csv("Players.csv")
# 1- İlk 10 kaydı getiriniz.
result = df.head(10)
# 2- Toplam kaç kayıt vardır?
result = len(df.index)
# 3- Tüm oyuncuların toplam maaş ortalaması nedir?
result = df["height"].mean()  #!bende maaş bilgisi olmadığı için boy ortalamalarını aldım!
# 4- En yüksek maaş ne kadardır?
result = df["weight"].max()
# 5- En yüksek maaşı alan oyuncu kimdir?
result = df[df["weight"] == df["weight"].max()]["Player"]  #indeksle beraber geliyor sonuna .iloc[0] yazarsak sadece ismi gelir
# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takım bilgileri nelerdir?
result = df[(df["born"] >= 1970) & (df["born"] <= 1975)][["Player","collage"]]
# 7- "John Holland" isimli oyuncunun oynadığı takım hangisidir?
result = df[df["Player"] == "Kobe Bryant"]["collage"]
# 8- Takımlara göre oyuncuların ortalama maaş bilgisi nedir?
# 9- Kaç farklı takım mevcut?
result = len(df.groupby("collage"))
result = df["collage"].nunique()
# 10- Her takımda kaç oyuncu oynamaktadır?
result = df["collage"].value_counts()
# 11- İsmi içinde "and" geçen kayıtları bulunuz.
df = df.dropna()

# result = df[df["Player"].str.contains("and")]
def str_find(Player):
    if "and" in Player.lower():
        return True
    return False
result = df[df["Player"].apply(str_find)]

print(result)