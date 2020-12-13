# Picos e vales

import sys

n = int(input())
string = input().split(" ")
tipo = ""
tipoAnt = ""

for i in range(1, len(string)):
    aux = int(string[i])
    ant = int(string[i-1])

    if aux > ant:
        tipo = "pico"
    elif aux < ant:
        tipo = "vale"

    if tipoAnt == tipo:
        print(0)
        sys.exit()
    tipoAnt = tipo

print(1)