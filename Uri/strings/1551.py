# Frase Completa

n = int(input())

for i in range(0, n):
    letras = []
    for j in range(0, 26):
        letras.append(False)

    string = input()

    for j in range(0, len(string)):
        if 97 <= ord(string[j]) <= 122 and letras[ord(string[j]) - 97] is False:
            letras[ord(string[j]) - 97] = True;

    cont = 0
    for j in range(0, 26):
        if letras[j] is True:
            cont += 1

    if cont == 26:
        print("frase completa")
    elif cont >= 13:
        print("frase quase completa")
    else:
        print("frase mal elaborada")