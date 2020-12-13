# Sequência de Sequência

caso = 1

while True:
    try:
        seq = [0]
        n = int(input())
        qtd = 0

        if n != 0:
            seq.append(1)
            for i in range(2, n+1):
                for j in range(0, i):
                    seq.append(i)

        if len(seq) > 1:
            print("Caso {}: {} numeros".format(caso, len(seq)))
        else:
            print("Caso {}: {} numero".format(caso, len(seq)))

        for i in range(0, len(seq)):
            if i == len(seq)-1:
                print(seq[i])
            else:
                print(seq[i], end=" ")

        print("")
        caso += 1

    except EOFError:
        break
