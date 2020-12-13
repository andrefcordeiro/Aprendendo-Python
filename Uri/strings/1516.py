# Imagem

firstLine = True

while True:

    if firstLine is False:
        print()

    else:
        firstLine = False

    string = input().split(" ")
    n = int(string[0])
    m = int(string[1])

    if n == 0 and m == 0:
        break

    desenho = [] #possui cada caractere

    for i in range(0, n):
        linha = input()
        desenho.append(linha)

    #print(desenho)

    string = input().split(" ")
    a = int(string[0])
    b = int(string[1])

    #printando redimensionado
    for i in range(0, len(desenho)):
        for j in range(0, int(a/n)): #printando c/ linha a/n vezes
            linha = desenho[i]
            for c1 in range(0, len(linha)):
                for c2 in range(0, int(b/m)): #printando c/ caracter b/m vezes
                    print(linha[c1], end="")
            print()