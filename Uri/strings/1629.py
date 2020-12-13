# Descompacta Face

def soma(intStr):
    soma = 0

    for i in range(0, len(intStr)):
        soma += int(intStr[i])

    return soma

while True:
    n = int(input())

    if n == 0:
        break

    for i in range(0, n): #le cada visitante
        d = 0 # 1 ou 0
        num = input()
        cont0 = 0
        cont1 = 0

        for j in range(0, len(num)): #itera cada digito
            for c in range(0, int(num[j])):
                if d == 0:
                    cont0 += 1
                else:
                    cont1 += 1

            if d == 1:
                d = 0
            else:
                d = 1

        soma0 = soma(str(cont0))
        soma1 = soma(str(cont1))
        print(soma0 + soma1)