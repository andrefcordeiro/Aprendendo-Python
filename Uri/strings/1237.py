# Comparação de Substring

while True:
    try:
        str1 = input()
        str2 = input()
        tamMaior = 0 # tamanho da maior subsequencia

        for i in range(0, len(str1)):
            for j in range(i, len(str1)):
                subs = str1[i:j+1]
                #print(subs, end=" ")

                if subs in str2:
                    if tamMaior == 0: #tamanho inicial
                        tamMaior = len(subs)

                    elif len(subs) > tamMaior:
                        tamMaior = len(subs)

                    if j == len(str1) - 1: # se for a ultima substring da linha, a prox não podera ser maior
                        break

            #print()
        print(tamMaior)

    except EOFError:
        break