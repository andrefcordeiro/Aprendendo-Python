# Chirrin Chirrion

casos = int(input())

for i in range(0, casos):
    n = int(input())
    total = []

    for c in range(0, n):
        linha = input().split()
        coisa = linha[0]
        acao = linha[1]

        if acao == "chirrin" and coisa not in total:
            total.append(coisa)

        elif acao == "chirrion" and coisa in total:
            total.pop(total.index(coisa))

    total.sort()
    print("TOTAL")
    for c in range(0, len(total)):
        print(total[c])