# Combinador

n = int(input())

for i in range(0, n):
    str = input().split(" ")
    str1 = str[0]
    str2 = str[1]
    str = []

    if len(str1) >= len(str2):
        for j in range(0, len(str1)):
            str.append(str1[j])
            if j < len(str2):
                str.append(str2[j])
    else:
        for j in range(0, len(str2)):
            if j < len(str1):
                str.append(str1[j])
            str.append(str2[j])

    strfinal = ''.join(str)
    print(strfinal)