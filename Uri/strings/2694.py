# Problema com a Calculadora

n = int(input())

for i in range(0, n):
    string = input()
    print(int(string[2:4]) + int(string[5:8]) + int(string[11:13]))