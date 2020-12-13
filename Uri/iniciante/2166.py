# Raiz quadrada de 2

n = int(input())
x = 0

for i in range(0, n):
    x += 2
    x = 1 / x
x += 1

print("{:.10f}".format(x))
