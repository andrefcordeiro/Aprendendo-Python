# De quem é a vez?

qtd = int(input())

for i in range(0, qtd):
    linha = input().split()
    j1 = linha[0]
    jog1 = linha[1]
    j2 = linha[2]
    jog2 = linha[3]

    linha = input().split()
    n1 = int(linha[0])
    n2 = int(linha[1])

    if (n1 + n2) % 2 == 0:
        if jog1 == "PAR":
            print(j1)
        else:
            print(j2)
    else:
        if jog1 == "IMPAR":
            print(j1)
        else:
            print(j2)
