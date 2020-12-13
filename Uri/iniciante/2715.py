# Dividindo os trabalhos

# soma à partir do indice
def somaAPartir(ini, fim, vetor):
    soma = 0
    for c in range(ini, fim):
        if type(vetor[c]) == int or type(vetor[c]) == float:
            soma += vetor[c]

    return soma


while True:
    try:
        n = int(input())
        vetor = input().split(" ")

        for i in range(0, len(vetor)):
            if vetor[i].isnumeric() is True:
                vetor[i] = int(vetor[i])

        # rangel
        iniR = 0
        fimR = 1
        # gugu
        iniG = 1
        fimG = len(vetor)

        if len(vetor) == 1:
            dif = 1

        else:
            while True:
                soma1 = somaAPartir(iniR, fimR, vetor)
                soma2 = somaAPartir(iniG, fimG, vetor)
                dif = abs(soma1 - soma2)

                if (type(vetor[fimR-1]) == int or type(vetor[fimR-1]) == float) and type(vetor[iniG-1]) == int or type(vetor[iniG-1]) == float:
                    difMenos1 = abs((soma1 - vetor[fimR-1]) - (soma2 + vetor[iniG-1]))

                if difMenos1 < dif:
                    dif = difMenos1
                    break

                else:
                    fimR += 1
                    iniG += 1

        print("{:.0f}".format(dif))

    except EOFError:
        break