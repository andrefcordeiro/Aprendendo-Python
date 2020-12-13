# Aproveite a oferta

t = int(input())

for i in range(0, t):
    linha = input().split()
    n = int(linha[0])
    k = int(linha[1])

    resto = n % k #garrafas não trocadas
    div = n // k #garrafas ganhas pela troca
    print(resto + div)