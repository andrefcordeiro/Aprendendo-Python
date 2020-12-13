# PãodeQuejoSweeper

def qtdPaesEnvolta(i, j, mat):
    cont = 0

    if i == 0 or i == len(mat)-1:
        if i == 0 and len(mat) > 1: #primeira linha
            if mat[i + 1][j] == 1:
                cont += 1

        elif i == len(mat)-1 and len(mat) > 1: #ultima linha
            if mat[i - 1][j] == 1:
                cont += 1

        if j == 0 and len(mat[i]) > 1:
            if mat[i][j + 1] == 1:
                cont += 1

        elif j == len(mat[i])-1 and len(mat[i]) > 1:
            if mat[i][j - 1] == 1:
                cont += 1

        else:
            if len(mat[i]) == 1 and i == 0:
                if mat[i][j + 1] == 1:
                    cont += 1

            elif len(mat[i]) == 1 and i == len(mat[i]) - 1:
                if mat[i][j - 1] == 1:
                    cont += 1

            else:
                if mat[i][j - 1] == 1:
                    cont += 1
                if mat[i][j + 1] == 1:
                    cont += 1

    else:
        if mat[i+1][j] == 1:
            cont += 1
        if mat[i - 1][j] == 1:
            cont += 1

        if j == len(mat[i]) - 1:
            if mat[i][j - 1] == 1:
                cont += 1

        elif j == 0:
            if mat[i][j + 1] == 1:
                cont += 1

        else:
            if mat[i][j - 1] == 1:
                cont += 1
            if mat[i][j + 1] == 1:
                cont += 1

    return cont


while True:

    try:
        string = input().split(" ")
        n = int(string[0])
        m = int(string[1])
        mat = []

        for i in range(0, n):  # lendo a matriz (vetor onde cada pos tb é um vetor)
            linha = input().split(" ")
            for j in range(0, m):
                linha[j] = int(linha[j])
            mat.append(linha)

        for i in range(0, n):
            for j in range(0, m):
                if mat[i][j] == 1:
                    print(9, end="")
                else:
                    print(qtdPaesEnvolta(i, j, mat), end="")

            print()

    except EOFError:
        break
