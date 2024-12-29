# # key - value
# # 41 bilgisi bize kocaelini verir 34 bilgisi de istanbulu

# sehirler = ["kocaeli","istanbul"]
# plakalar = [41,34]

# print(plakalar[sehirler.index("kocaeli")])

# # print(plakalar["kocaeli"]) => 41 
# # print(plakalar["istanbul"]) =>) => 34

# plakalar = {"kocaeli":41, "istanbul":34}
# print(plakalar["kocaeli"])
# print(plakalar["istanbul"])  

# plakalar["ankara"] = 6
# print(plakalar)


users = {
    "sadikturan" :{
    "roles": ["user"],
    "age" : 36,
    "email": "sadik@gmail.com",
    "address": "kocaeli",
    "phone" : "123123"
    },
    "cinarturan":{
    "roles":["admin","user"],
    "age" : 2,
    "email":"cinar@gmail.com",
    "address":"kocaeli",
    "phone" : "123456"
    }
}

print(users["cinarturan"]["roles"][0])

# print(users["cinarturan"]["age"])
# print(users["cinarturan"]["email"])
# print(users["cinarturan"]["phone"])