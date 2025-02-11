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

def getProducts():
    connection = mysql.connector.connect(host="localhost",user = "root",password ="***",database ="node-app")
    cursor = connection.cursor()
    
   # cursor.execute ("Select * From products")  # * işaretiyle bütün kolonları kastediyoruz
    cursor.execute("Select name,price From Products")

    # result = cursor.fetchall()  #birden fazla kayıt almak istediğimiz zaman kullanılan metot
    result = cursor.fetchone()  #bulduğu ilk kaydı getirir
    print(print(f"name:{result[0]} price: {result[1]}")
)

    # for product in result:
    #     # print(f"name:{product[1]} price: {product[2]}")
    #     print(f"name:{product[0]} price: {product[1]}")

getProducts()
