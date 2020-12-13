# Pegadinha de Evergreen

def printaArrayComoString(array):
    for j in range(0, len(array)):
        if j == len(array)-1:
            print(array[j])
        else:
            print(array[j], end="")

n = int(input())

for c in range(0, n):
    str1 = input()
    str2 = input()
    nome = []

    i = 0

    while i < len(str1):

        nome.append(str1[i:i+2])
        if i == len(str2) - 1:
            nome.append(str2[i])
        else:
            nome.append(str2[i:i+2])

        i += 2

    printaArrayComoString(nome)