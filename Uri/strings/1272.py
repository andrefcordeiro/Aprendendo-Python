# Mensagem Oculta

def printaCharArrayComoString(charArray):
    for j in range(0, len(charArray)):
        if j == len(charArray)-1:
            print(charArray[j])
        else:
            print(charArray[j], end="")

n = int(input())

for i in range(0, n):
    string = input()
    primeirasLetras = []
    frase = False

    for j in range(0, len(string)):
        if ord(string[j]) != 32 and frase is False:
            primeirasLetras.append(string[j])
            frase = True

        if ord(string[j]) == 32:
            frase = False

    printaCharArrayComoString(primeirasLetras)