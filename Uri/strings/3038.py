# Carta de natal criptografada

while True:
    try:
        frase = list(input())

        for i in range(0, len(frase)):
            if frase[i] == "@":
                frase[i] = "a"
            elif frase[i] == "&":
                frase[i] = "e"
            elif frase[i] == "!":
                frase[i] = "i"
            elif frase[i] == "*":
                frase[i] = "o"
            elif frase[i] == "#":
                frase[i] = "u"

        for i in range(0, len(frase)):
            if i == len(frase) - 1:
                print(frase[i])
            else:
                print(frase[i], end="")
    except EOFError:
        break
