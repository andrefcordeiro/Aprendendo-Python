# Hora da Corrida

input = input().split(" ")
voltas = int(input[0])
placas = int(input[1])

razao = int((voltas*placas)/9)
valor = razao

for i in range(0, 9):
    if i == 8:
        print(valor)
    else:
        print(valor, end=" ")
    valor += razao
