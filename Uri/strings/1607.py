# Avance as letras

n = int(input())

for i in range(0, n):
    string = input().split(" ")
    a = string[0]
    b = string[1]

    c = 0
    for j in range(0, len(a)):
        aux = ord(a[j])
        while aux != ord(b[j]):
            if aux >= 122:
                aux = 97
            else:
                aux += 1
            c += 1

    print(c)