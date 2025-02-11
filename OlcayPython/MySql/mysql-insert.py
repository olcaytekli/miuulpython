import mysql.connector

def insertProduct(name,price,imageURL,description):
    connection = mysql.connector.connect(host ="localhost",user="root",password="****",database="node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO products(name,price,imageURL,description) VALUES (%s,%s,%s,%s)"
    values = (name,price,imageURL,description) #kendi elimizle de veri girebilirdik fakat bu veriyi kullancıdan aldırır

    cursor.execute(sql,values)
    
    try:
        connection.commit()  #Sorguladığımız bilgileri database'e gönderiyor
        print(f"{cursor.rowcount} tane kayıt eklendi") 
        print(f"son eklenen kaydın id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata:",err)
    
    finally:
        connection.close()
        print("database bağlantısı kapandı.")

def insertProducts(list):
    connection = mysql.connector.connect(host ="localhost",user="root",password="****",database="node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO products(name,price,imageURL,description) VALUES (%s,%s,%s,%s)"
    values = list

    cursor.executemany(sql,values)
    
    try:
        connection.commit()  #Sorguladığımız bilgileri database'e gönderiyor
        print(f"{cursor.rowcount} tane kayıt eklendi") 
        print(f"son eklenen kaydın id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata:",err)
    
    finally:
        connection.close()
        print("database bağlantısı kapandı.")




#birden fazla kayıt eklemek istediğimin zaman while döngüsü
list=[]
while True:
    name = input("ürün adı:")
    price = float(input("ürün fiyatı:"))
    imageURL = input("ürün resim adı:")
    description = input("ürün açıklaması:")

    list.append((name,price,imageURL,description))

    result = input("devam etmek istiyor musunuz? (e/h)")
    if result == "h":
        print("Kayıtlarınız veritabanına aktarılıyor...")
        print(list)
        insertProducts(list)
        break

#insertProduct(name,price,imageURL,description)

    