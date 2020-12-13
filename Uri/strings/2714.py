# Minha Senha Provisória

n = int(input())

for i in range(0, n):
    linha = input()

    if len(linha) == 20 and linha[0] == 'R' and linha[1] == 'A':
        lastIndex = 1
        for c in range(2, len(linha)):
            if linha[c] == "0":
                lastIndex = c #ultimo zero
            else:
                break

        print(linha[lastIndex+1:])

    else:
        print("INVALID DATA")