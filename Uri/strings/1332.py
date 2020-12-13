# um Dois Três

#encontra a qtd de letras diferentes de charArray1 e charArray2, verificando tambem se as iguais estao na msm posição
def qtdDeLetrasDiferentes(charArray1, charArray2):
    qtdDif = 0
    for i in range(0, len(charArray1)):
        if charArray1[i] != charArray2[i]:
            qtdDif += 1

    return qtdDif

n = int(input())

for i in range(0, n):
    one = ['o', 'n', 'e']
    two = ['t', 'w', 'o']
    three = ['t', 'h', 'r', 'e', 'e']
    num = input()
    charArray = []

    for j in range(0, len(num)):
        charArray.append(num[j])

    cont = 0
    if len(charArray) == 3:

        if qtdDeLetrasDiferentes(charArray, two) > 1:
            print(1)
        else:
            print(2)

    else:
        print(3)

