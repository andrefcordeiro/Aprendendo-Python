# Nova Senha

def printaArrayComoString(array):
    for j in range(0, 12):
        if j == 11:
            print(array[j])
        else:
            print(array[j], end="")


def codifica(letra):
    ult = str(ord(letra[len(letra)-1]))
    ult = ult[len(ult)-1] #ultimo char

    #print(letra, ult)

    if letra.islower():
        if ult == "7":
            return "0"
        elif ult == "8":
            return "1"
        elif ult == "9":
            return "2"
        elif ult == "0":
            return "3"
        elif ult == "1":
            return "4"
        elif ult == "2":
            return "5"
        elif ult == "3":
            return "6"
        elif ult == "4":
            return "7"
        elif ult == "5":
            return "8"
        elif ult == "6":
            return "9"
    else:
        if ult == "1":
            return "0"
        elif ult == "3":
            return "1"
        elif ult == "9":
            return "2"
        elif ult == "0":
            return "3"
        elif ult == "4":
            return "4"
        elif ult == "8":
            return "5"
        elif ult == "5":
            return "6"
        elif ult == "7":
            return "7"
        elif ult == "6":
            return "8"
        elif ult == "2":
            return "9"


n = int(input())

for i in range(0, n):
    senha = input()
    num = []

    for c in range(0, len(senha)):
        if senha[c] != " ":
            num.append(codifica(senha[c]))

    printaArrayComoString(num)