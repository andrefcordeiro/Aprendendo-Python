# Justificador 2

def retiraEspacosDesnec(string):
    charArray = []
    ant = ""

    for i in range(0, len(string)):
        if i == 0:
            ant = string[i]
            if string[i] != " ":
                charArray.append(string[i])

        elif (ant != " " and string[i] != " ") or (ant == " " and string[i] != " ") or (ant != " " and string[i] == " "):
            charArray.append(string[i])
            ant = string[i]

    return "".join(charArray)


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
        palavras.append(retiraEspacosDesnec(string).strip())

        if i == 0:
            maiorTam = len(palavras[i])

        elif maiorTam < len(palavras[i]):
            maiorTam = len(palavras[i])

    for i in range(0, len(palavras)):
        print((maiorTam - len(palavras[i]))*" " + palavras[i])
