# De dentro para fora

n = int(input())

for i in range(0, n):
    str = input()

    for j in range(int((len(str)/2)) - 1, -1, -1):
        print(str[j], end="")

    for j in range(len(str)-1, int((len(str)/2)) - 1, -1):
        print(str[j], end="")

    print()