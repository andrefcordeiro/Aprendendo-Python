# Obi Uri2

n = int(input())

linha = input().split()

for i in range(0, len(linha)):
    if len(linha[i]) == 3:
        if linha[i][0] == 'U' or linha[i][0] == 'O' and linha[i][2] != "I":
            lista = list(linha[i])
            lista[2] = "I"
            linha[i] = "".join(lista)

print(" ".join(linha))