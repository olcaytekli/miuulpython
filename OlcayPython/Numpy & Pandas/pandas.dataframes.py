# dataframe serilerin bir devamı olarak görülebilir yani iki serinin toplamı bir dataframe eder
# dataframe üzerinden sorgulama yapabiliyoruz

import pandas as pd
list = [["Ahmet",50],["Ali",60],["Yağmur",70],["Çınar",80]]
dict = {"Name":["Ahmet","Ali","Yağmur","Çınar"],"Grade": [50,60,70,80]}

#iki data bilgisini bir liste içinde barındırm
dict_list = [
             {"Name":"Ahmet","Grade":50},
             {"Name":"Ali","Grade":60},
             {"Name":"Yağmur","Grade":70},
             {"Name":"Çınar","Grade":80}
             ]


# df = pd.DataFrame()
# df = pd.DataFrame([1,2,3,4])
# df = pd.DataFrame(list,index = [1,2,3,4], columns = ["Name","Grade"])
# df = pd.DataFrame(dict)
# df = pd.DataFrame(dict, index = ["212","232","236","456"])
# df = pd.DataFrame(dict_list)
df = pd.DataFrame(dict_list,index = ["212","232","236","456"])

print(df)



# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2])

# data = dict(apples = s1, oranges = s2)  #data isimli bir dict içine aldık #apples ve oranges bilgileri bize kolon bilgisi olarak geldi

# df = pd.DataFrame(data)

# print(df)