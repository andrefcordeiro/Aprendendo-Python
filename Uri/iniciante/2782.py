# Escadinha

n = int(input())
linha = input().split()

if n <= 2:
    print(n)

else:
    qtdEsc = 1 #quantidade de "escadinhas"
    isEsc = True #a sequencia está em uma escadinha, os 2 primeiros termos juntos já sao uma
    dif = int(linha[1]) - int(linha[0])

    for i in range(2, len(linha)):
        if isEsc is True: #se uma sequencia escadinha está "rolando"
            if int(linha[i]) - int(linha[i-1]) != dif: #se a diferença não for a mesma
                dif = int(linha[i]) - int(linha[i-1]) #inicia-se uma nova escadinha
                qtdEsc += 1

        elif isEsc is False: #primeiro da sequencia escadinha
            dif = int(linha[i]) - int(linha[i-1])
            isEsc = True
            qtdEsc += 1
        else: #se não é uma sequencia correta
            isEsc = False

    print(qtdEsc)