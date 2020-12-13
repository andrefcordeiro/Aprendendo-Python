# Matriz Quadrada III

while True:
    n = int(input())

    if n == 0:
        break

    t = 1
    if n > 1:
        for i in range(1, n):
            t = t*4

    valorInicial = 1 #valor inicial da sequencia
    aux = 1
    for i in range(0, n):
        for j in range(0, n):
            if j == n-1:
                print("{:{}}".format(valorInicial, len(str(t))))
            else:
                print("{:{}}".format(valorInicial, len(str(t))), end=" ")

            if j == 1:
                aux = valorInicial
            valorInicial = 2*valorInicial
        valorInicial = aux
    print()