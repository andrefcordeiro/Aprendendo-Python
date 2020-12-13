# Kikoho

import math


def determinante3x3(x1, y1, x2, y2, x3, y3):
    determinante = x1*y2*1 + y1*1*x3 + 1*x2*y3 - (1*y2*x3) - (x1*1*y3) - (y1*x2*1)

    return math.fabs(determinante)

n = int(input())

for i in range(0, n):
    str = input().split(" ")
    x1 = int(str[0])
    y1 = int(str[1])
    x2 = int(str[2])
    y2 = int(str[3])
    x3 = int(str[4])
    y3 = int(str[5])

    print("{:.3f}".format( (1/2) * determinante3x3(x1, y1, x2, y2, x3, y3)))