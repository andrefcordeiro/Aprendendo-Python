# Conjuntos bons e ruins

#string1 é prefixo de string2 ?
def isPrefixo(string1, string2):
    str2 = string2[0:len(string1)]

    if string1 == str2:
        return 1

    return 0


while True:
    n = int(input())
    if n == 0:
        break

    palavras = []
    isBad = 0

    for i in range(0, n):
        pal = input()
        palavras.append(pal)
        if isBad == 0:
            for j in range(0, len(palavras)):
                if i != j:
                    if isPrefixo(palavras[i], palavras[j]) or isPrefixo(palavras[j], palavras[i]):
                        isBad = 1
                        break

    if isBad == 1:
        print("Conjunto Ruim")
    else:
        print("Conjunto Bom")
