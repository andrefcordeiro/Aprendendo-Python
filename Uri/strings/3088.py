# Correção de texto

def printaArrayComoString(array):
    for j in range(0, len(array)):
        if j == len(array)-1:
            print(array[j])
        else:
            print(array[j], end="")


while True:
    try:
        string = input()
        array = []

        for i in range(0, len(string)):
            array.append(string[i])
            if i != len(string) - 1:
                if string[i] == " ":
                    if string[i+1] == "," or string[i+1] == ".":
                        array.pop()

        printaArrayComoString(array)
    except EOFError:
        break