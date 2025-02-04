import mysql.connector

def insertProduct(name,price,imageURL,description):
    connection = mysql.connector.connect(host ="localhost",user="root",password="mysql123",database="node-app")
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
    connection = mysql.connector.connect(host ="localhost",user="root",password="mysql123",database="node-app")
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
    connection = mysql.connector.connect(host="localhost",user = "root",password ="mysql123",database ="node-app")
    cursor = connection.cursor()
    
    # cursor.execute("Select * From products Where id = 1")  # * işaretiyle bütün kolonları kastediyoruz ve where ile filtreleme yaparız
    # cursor.execute("Select * From products Where name = 'Samsung s8'and price=3000")
    # cursor.execute("Select * From products Where name LIKE '%Samsung%'")  #samsung geçenleri getirme
    # cursor.execute("Select * From products Where name LIKE '%Samsung%' and price =3000") 
    # cursor.execute("Select * From products Order By name")  #sıralama işlemi isme göre fiyata göre vs ne istersek
    cursor.execute("Select * From products Order By price DESC")  #azalan bir şekilde sıralama için

    result = cursor.fetchall()  #birden fazla kayıt almak istediğimiz zaman kullanılan metot
    
    for product in result:
         print(f"id: {product[0]} name:{product[1]} price: {product[2]}")




def getProductsId(id):
    connection = mysql.connector.connect(host="localhost",user = "root",password ="mysql123",database ="node-app")
    cursor = connection.cursor()

    sql = "Select * From Products Where id=%s"
    params=(id,)

    cursor.execute(sql,params)

    result = cursor.fetchone()

    print(f"id: {result[0]} name:{result[1]} price: {result[2]}")

def updateProduct(id, name, price):
    connection = mysql.connector.connect(host="localhost",user = "root",password ="mysql123",database ="node-app")
    cursor = connection.cursor()

    # sql = "Update products Set name ='Samsung s10',price = 5000 where id = 5" #IDsi 5 olan kaydı güncelledik
    sql = "Update products Set name = %s, price = %s where id= %s"
    values = (name,price,id)
    cursor.execute(sql,values)

    try:
        connection.commit()  #Sorguladığımız bilgileri database'e gönderiyor
        print(f"{cursor.rowcount} tane kayıt eklendi") 
    except mysql.connector.Error as err:
        print("hata:",err)
    
    finally:
        connection.close()
        print("database bağlantısı kapandı.")

# updateProduct(1, "Iphone 8",6000)

def deleteProduct(id):
    connection = mysql.connector.connect(host="localhost",user = "root",password ="mysql123",database ="node-app")
    cursor = connection.cursor()

    # sql = "delete from products" #böyle bütün kayıtları sileriz
    # sql = "delete from products where id=6" # id si 6 olan kaydı sileriz
    # sql = "delete from products where name like '%s7%'" 
    sql = "delete from products where id = %s"
    values = (id,)
    cursor.execute(sql,values)

    try:
        connection.commit()  #Sorguladığımız bilgileri database'e gönderiyor
        print(f"{cursor.rowcount} tane kayıt silindi") 
    except mysql.connector.Error as err:
        print("hata:",err)
    
    finally:
        connection.close()
        print("database bağlantısı kapandı.")
# deleteProduct(5)
# getProducts()
