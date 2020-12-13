# Sequência Espelho

c = int(input())

for c in range(0, c):
    linha = input().split(" ")
    b = int(linha[0])
    e = int(linha[1])

    for i in range(b, e+1):
        print(i, end="")

    for i in range(e, b-1, -1):
        print(str(i)[::-1], end="") # printando string invertida
    print()