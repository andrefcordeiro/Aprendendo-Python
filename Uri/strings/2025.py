# Joulupukki

n = int(input())

for i in range(0, n):
    linha = input().split(" ")
    subs = "oulupukk"

    for c in range(0, len(linha)):
        lista = list(linha[c])

        if subs in linha[c]:
            if lista[0] != "J":
                lista[0] = "J"

            if len(lista) == 10:
                lista[len(lista)-1] = "i"

            elif len(lista) == 11:
                lista[len(lista)-2] = "i"

            linha[c] = "".join(lista)

    print(" ".join(linha))