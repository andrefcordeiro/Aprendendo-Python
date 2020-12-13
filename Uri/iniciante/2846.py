# Fibonot

import sys

n = int(input())
a = 1
b = 1
aux = 0

if n == 1:
    print(4)

else:
    cont = 0
    for i in range(0, n*2):
        aux = b
        b = b+a
        a = aux
        for j in range(a+1, b):
            cont += 1
            if cont == n:
                print(j)
                sys.exit()

