
while True:
    n = int(input())
    if n == 0:
        break

    entre = 1 #espaços entre duas hashtags
    for i in range(0, n):
        if i != 0:
            print((n-i)*' ', end="")
            print("#", end="")
            print(entre * ' ', end="")
            entre = entre+2
        else:
            print((n - i) * ' ', end="")
        print("#")

    entre = entre - 2

    for i in range(1, n):
        if i != n-1:
            print((i+1) * ' ', end="")
            print("#", end="")
            entre = entre - 2
            print(entre * ' ', end="")
        else:
            print((i+1) * ' ', end="")
        print("#")


