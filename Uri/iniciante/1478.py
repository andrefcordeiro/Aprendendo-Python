# Matriz Quadrada II

while True:
    n = int(input())

    if n == 0:
        break
    pos = 0 #posição do 1 na linha
    valorInicial = 1 #valor inicial da sequencia

    for i in range(0, n):
        for j in range(0, n):
            if j == n-1:
                print("{:3}".format(valorInicial))
            else:
                print("{:3}".format(valorInicial), end=" ")
            if j < pos:
                valorInicial -= 1
            elif j >= pos:
                valorInicial += 1
        pos += 1
        valorInicial = pos + 1
    print()