# Variações

t = int(input())

for i in range(0, t):
    senha = input()
    combinacoes = 1

    for c in range(0, len(senha)):
        s = senha[c].lower()

        if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 's':
            combinacoes *= 3
        else:
            combinacoes *= 2

    print(combinacoes)



