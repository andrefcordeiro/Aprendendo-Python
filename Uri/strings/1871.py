# Zero vale Zero

def retiraZero(numInteiro):
    numStr = str(numInteiro)
    digitos = []

    for i in range(0, len(numStr)):
        if numStr[i] != '0':
            digitos.append(numStr[i])

    return int(''.join(digitos))


while True:
    string = input().split(" ")
    n = int(string[0])
    m = int(string[1])

    if n == 0 and m == 0:
        break

    print(retiraZero(retiraZero(n) + retiraZero(m)))


