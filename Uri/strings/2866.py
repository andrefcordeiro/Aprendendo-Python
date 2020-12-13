# Criptotexto

n = int(input())

for i in range(0, n):
    string = input()
    texto = []

    for c in range(0, len(string)):
        if string[c].islower():
            texto.append(string[c])

    texto.reverse()
    texto = "".join(texto)
    print(texto)
