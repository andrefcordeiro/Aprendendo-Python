# Criptografia

def printaCharArrayComoString(charArray):
    for j in range(0, len(charArray)):
        if j == len(charArray)-1:
            print(charArray[j])
        else:
            print(charArray[j], end="")

n = int(input())

for i in range(0, n):
    string = input()
    charArray = []

    for j in range(0, len(string)):
        if 65 <= ord(string[j]) <= 90 or 97 <= ord(string[j]) <= 122:
            charArray.append(chr(ord(string[j])+3))
        else:
            charArray.append(string[j])

    charArray.reverse()
    charArrayFinal = []
    for j in range(0, len(charArray)):
        if j >= int(len(charArray)/2):
            charArrayFinal.append(chr(ord(charArray[j])-1))
        else:
            charArrayFinal.append(charArray[j])

    printaCharArrayComoString(charArrayFinal)
