# Justificador

quebraLinha = False

while True:
    n = int(input())
    if n == 0:
        break

    if quebraLinha is False:
        quebraLinha = True

    elif quebraLinha is True:
        print()

    maiorTam = 0
    palavras = []

    for i in range(0, n):
        string = input()
        if i == 0:
            maiorTam = len(string)

        elif maiorTam < len(string):
            maiorTam = len(string)

        palavras.append(string)

    for i in range(0, len(palavras)):
        print((maiorTam - len(palavras[i]))*" " + palavras[i])
