# Idade da Dona Mônica

m = int(input())
a = int(input())
b = int(input())

if m - (a+b) > a and m - (a+b) > b:
    print(m - (a+b))

elif a > b:
    print(a)

else:
    print(b)