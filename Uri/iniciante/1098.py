# Sequência de IJ 4

i = 0
j = 1
c = 0
aux = i

while i < 2:
    if (i == 1 or round(i, 0) == 2 or i == 0) and round(i, 1) != 1.6 and round(i, 1) != 1.8:
        print("I={:.0f}".format(i), end=" ")
    else:
        print("I={:.1f}".format(i), end=" ")

    if j == 1.0 or j == 2.0 or j == 3.0 or j == 4.0 or j == 5.0:
        print("J={:.0f}".format(j))
    else:
        print("J={:.1f}".format(j))

    c += 1
    if c == 3:
        j = aux + 0.2
        aux = j
        i += 0.2
        c = 0
    j += 1