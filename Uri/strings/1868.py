# Espiral Quadrada

while True:
    n = int(input())

    if n == 0:
        break

    xPosI = int(n / 2)  # utilizando indices que se iniciam em [0, 0]
    xPosJ = int(n / 2)
    op = 2 #quantidade de operações em sequencia (em lin e col)
    sinalOpI = -1 #sinal das operações nas linhas (atualizado multiplicando por -1)
    sinalOpJ = +1 #sinal das operações nas colunas (atualizado multiplicando por -1)
    cont = 0 #itera a qtd de operações

    for c in range(0, n * n):  # n*n tabelas

        for i in range(0, n):  # linhas
            for j in range(0, n):  # colunas
                if i == xPosI and j == xPosJ:
                    print("X", end="")
                else:
                    print("O", end="")
            print()
        print("@")

        if cont < op/2:
            xPosJ += sinalOpJ
            cont += 1
        elif cont < op:
            xPosI += sinalOpI
            cont += 1
        if op == cont:
            cont = 0
            sinalOpJ *= -1
            sinalOpI *= -1
            op += 2
