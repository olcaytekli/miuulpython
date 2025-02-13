### UYGULAMA-MÜLAKAT SORUSU###

# Amaç : Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.

#before: "hi my name is john and i am learning python"
#after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

range(len("miuul"))   #range(0,5)

def alternating(string):
    new_string = ""
    # girilen string'in indexlerinde gez.
    for string_index in range(len(string)):
        #index çift ise büyük harfe çevir
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        #index tek ise küçük harfe çevir
        else:
            new_string += string[string_index].lower()
    print(new_string)

alternating("hi my name is john and i am learning python")






#### Uygulama - Mülakat Sorusu ###

# divide_students fonksiyonu yazınız.
# Çift indexte yer alan öğrencileri bir listeye alınız.
# Tek indexte yer alan öğrencileri başka bir listeye alınız.
# Fakat bu iki liste tek bir liste olarak return olsun.

students = ["John","Mark","Venessa","Mariam"]

def divide_students(students):
    groups = [[],[]]
    for index,student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else: groups[1].append(student)
    print(groups)
    return groups
divide_students(students)


