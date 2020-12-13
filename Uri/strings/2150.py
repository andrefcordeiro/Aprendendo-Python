# Vogais Alienígenas

while True:
    try:
        vogais = input()
        frase = input()
        cont = 0

        for i in range(0, len(frase)):
            if frase[i] in vogais:
                cont += 1
        print(cont)

    except EOFError:
        break