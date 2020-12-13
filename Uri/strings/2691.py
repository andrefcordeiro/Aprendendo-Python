# O Matemático

n = int(input())

for i in range(0, n):
    string = input().split('x')
    a = int(string[0])
    b = int(string[1])

    for j in range(5, 11):
        print("{} x {} = {}".format(a, j, a*j), end="")
        if b != a:
            print(" && {} x {} = {}".format(b, j, b * j))
        else:
            print()