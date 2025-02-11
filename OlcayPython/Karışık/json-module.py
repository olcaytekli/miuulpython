#Cihazlar arasında veri taşıma

import json

person_string = '{"name":"Ali","languages":["python","C#"]}'
person_dict = {"name":"Ali","languages":["Python","C#"]}

# JSON string to Dict

# result = json.loads(person_string)  #bu bizim personstringimizi bir dict. e çeviriyor
# result = result["name "]

# with open("person.json") as f:
#     data = json.load(f)
#     print(data["name"])
#     print(data["languages"])

person_dict = {
    "name" : "Ali",
    "languages" : ["Python","C#"]

}
# Dict to json string

# result = json.dumps(person_dict)
# print(result)
# print(type(result))

# with open("person.json","w") as f:  #dosyanın içine bilgiyi attık
#     json.dump(person_dict,f)

#PERSON STRİNGİ DİC. ÇEVİRME

person_dict = json.loads(person_string)

result = json.dumps(person_dict, indent=4,sort_keys = True)
print(person_dict)
print(result)