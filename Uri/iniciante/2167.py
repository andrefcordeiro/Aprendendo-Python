# Falha de Motor

import sys

n = input()
linha = input().split(" ")
ant = int(linha[0])

for i in range(1, len(linha)):
    if int(linha[i]) < ant:
        print(i+1)
        sys.exit()
    ant = int(linha[i])

print(0)
