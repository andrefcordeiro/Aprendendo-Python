# Conversa Internacional

n = int(input())

for i in range(0, n):
    numPess = int(input())
    idiomaAnt = []
    idioma = []
    mesmoIdioma = 1

    for i in range(0, numPess):
        idioma = input()
        if i != 0:
            if idioma != idiomaAnt:
                mesmoIdioma = 0

        idiomaAnt = idioma

    if mesmoIdioma == 0:
        print("ingles")
    else:
        print(idioma)