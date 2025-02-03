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

# def getProducts():
#     connection = mysql.connector.connect(host="localhost",user = "root",password ="***",database ="node-app")
#     cursor = connection.cursor()
    
#     # cursor.execute("Select * From products Where id = 1")  # * işaretiyle bütün kolonları kastediyoruz ve where ile filtreleme yaparız
#     # cursor.execute("Select * From products Where name = 'Samsung s8'and price=3000")
#     # cursor.execute("Select * From products Where name LIKE '%Samsung%'")  #samsung geçenleri getirme
#     cursor.execute("Select * From products Where name LIKE '%Samsung%' and price =3000") 
#     result = cursor.fetchall()  #birden fazla kayıt almak istediğimiz zaman kullanılan metot
    
#     print(result)

#     # for product in result:
#     #      print(f"id: {product[0]} name:{product[1]} price: {product[2]}")


# getProducts()

def getProductsId(id):
    connection = mysql.connector.connect(host="localhost",user = "root",password ="***",database ="node-app")
    cursor = connection.cursor()

    sql = "Select * From Products Where id=%s"
    params=(id,)

    cursor.execute(sql,params)

    result = cursor.fetchone()

    print(f"id: {result[0]} name:{result[1]} price: {result[2]}")

def getProductInfo():
    connection = mysql.connector.connect(host="localhost",user = "root",password ="mysql123",database ="node-app")
    cursor = connection.cursor()

    # sql = "Select COUNT(*) from Products"  #database de kaç tane kayıt varsa
    # sql = "Select AVG(price) FROM Products" #products tablosundaki fiyat alanının ortalama değeri
    # sql = "Select SUM(price) FROM Products"
    # sql = "Select MAX(price) FROM Products"
    # sql = "Select MIN(price) FROM Products"
    sql = "Select Name from Products where Price = (Select MAX(Price) from Products)" #en pahalının ismini getirme

    
    cursor.execute(sql)

    result = cursor.fetchone()

    print(f"result: {result[0]}")

getProductInfo()