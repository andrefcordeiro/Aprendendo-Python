# Teclado Zoeiro

def printaArrayComoString(array):
    for j in range(0, len(array)):
        if j == len(array)-1:
            print(array[j])
        else:
            print(array[j], end="")


linha = input().split()
n = int(linha[0])
m = int(linha[1])
letras = []
letTrocadas = []

for i in range(0, n):
    linha = input().split()
    letras.append(linha[0])
    letTrocadas.append(linha[1])

for i in range(0, m):
    linha = input()
    charArray = []
    for c in range(0, len(linha)):
        charArray.append(linha[c])

    for c in range(0, len(charArray)):
        if charArray[c] in letras:
            charArray[c] = letTrocadas[letras.index(charArray[c])]
        elif charArray[c] in letTrocadas:
            charArray[c] = letras[letTrocadas.index(charArray[c])]

    printaArrayComoString(charArray)