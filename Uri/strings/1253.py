# Cifra de Cesar

n = int(input())

for i in range(0, n):
    string = input()
    qtd = int(input())

    for c in range(0, len(string)):
        codLetra = ord(string[c])

        for j in range(0, qtd):
            codLetra -= 1

            if codLetra < 65:
                codLetra = 90

        print(chr(codLetra), end="")
    print()




