# Grace Hopper

while True:
    try:
        linha = input().lower().split("-")
        qtd = 0
        cobol = 'cobol'

        if len(linha) == 5:
            for i in range(0, len(linha)):
                if linha[i][0] == cobol[qtd] or linha[i][len(linha[i])-1] == cobol[qtd]:
                    qtd += 1

            if qtd == 5:
                print("GRACE HOPPER")
            else:
                print("BUG")
        else:
            print("BUG")

    except EOFError:
        break