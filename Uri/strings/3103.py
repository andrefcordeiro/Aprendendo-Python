# Numero da Sorte

t = int(input())

for i in range(0, t):
    num = list(input())
    num.sort()
    num.remove(num[0])

    if '0' in num:
        ini = num.index('0') #inicio e fim da sequencia de 0s
        fim = len(num) - num[::-1].index('0') - 1
        aux = num[fim+1]
        num[fim+1] = num[ini]
        num[ini] = aux

    for j in range(0, len(num)):
        if j == len(num) - 1:
            print(num[j])
        else:
            print(num[j], end="")