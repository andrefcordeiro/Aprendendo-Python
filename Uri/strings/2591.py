# HameKameKa

n = int(input())

for i in range(0, n):
    string = input().split("k")
    str1 = string[0]
    a = 0
    for j in range(0, len(str1)):
        if str1[j] == 'a':
            a += 1

    str2 = string[1]
    b = 0
    for j in range(0, len(str2)):
        if str2[j] == 'a':
            b += 1

    print("k{}".format("a"*(a*b)))