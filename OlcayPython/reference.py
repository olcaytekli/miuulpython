#value types => string, number
#y üzerinde yapacağım değişiklik x'i etkilemez.
x = 5
y = 25

x = y

y = 10

print(x,y)

#reference types => list
#b üzerinde yapacağım değişiklik a'yı etkiler.
a = ["apple","banana"]
b = ["apple","banana"]

a = b

b[0] = "grape"

print(a,b)