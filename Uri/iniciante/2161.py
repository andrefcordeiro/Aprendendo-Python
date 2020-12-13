# Raiz Quadrada de 10

n = int(input())
x = 0

for i in range(0, n):
    x += 6
    x = 1 / x
x += 3

print("{:.10f}".format(x))
