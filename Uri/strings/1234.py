# Sentença dançante

while True:
    try:
        str = input()
        strDancante = []
        antIsUp = -1 #anterior está em maiusculo

        for i in range(0, len(str)):
            charCode = ord(str[i])
            if charCode == 32: #espaco em branco
                strDancante.append(str[i])

            else:
                if antIsUp == -1: #primeiro caractere diferente de espaço
                    if charCode >= 97:
                        strDancante.append(str[i].upper())
                    else:
                        strDancante.append(str[i])
                    antIsUp = 1

                elif charCode >= 97: #se estiver em minuscula
                    if antIsUp == 0: #se o char anterior for minusculo
                        strDancante.append(str[i].upper())
                        antIsUp = 1
                    else:
                        strDancante.append(str[i])
                        antIsUp = 0

                elif charCode < 97: #se estiver em maiuscula
                    if antIsUp == 0:  # se o char anterior for minusculo
                        strDancante.append(str[i])
                        antIsUp = 1
                    else:
                        strDancante.append(str[i].lower())
                        antIsUp = 0

        for i in range(0, len(strDancante)):
            print(strDancante[i], end="")
        print()
    except EOFError:
        break
