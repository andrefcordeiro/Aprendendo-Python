# A Biblioteca do Senhor Severino

while True:
    try:
        num = []
        n = int(input())

        for i in range(0, n):
            linha = input()
            num.append(linha)

        num.sort()
        for i in range(0, n):
            print(num[i])

    except EOFError:
        break
