# Revisão de Contrato

def printaArrayComoString(array):
    for j in range(0, len(array)):
        if j == len(array)-1:
            print(array[j])
        else:
            print(array[j], end="")


while True:
    linha = input().split()
    d = linha[0]
    n = linha[1]

    if d == "0" and n == "0":
        break

    qtdZeros = 0
    printou = 0
    for i in range(0, len(n)):
        if n[i] != d and n[i] != '0':
            print(n[i], end="")
            printou = 1
        elif n[i] == '0' and printou == 1:
            qtdZeros += 1

    if printou == 0:
        qtdZeros = 1
    print("0"*qtdZeros)
