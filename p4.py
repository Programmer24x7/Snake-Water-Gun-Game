"""a = 1
b = 1
print(a==b)"""

a = 4
a += a
print(a)

d = 5==5
print(d)

#typecasting

a = 32
b = type(a)
print(b)
if type(a) == int:
    print("int")


a = int(input("A: "))
b = int(input("B: "))

print(a+b)
