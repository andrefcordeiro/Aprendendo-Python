# Iccanobif

n = int(input())
seqFib = []

seqFib.append(1)
seqFib.append(1)

if n == 1:
    print(1)

else:
    for i in range(1, n-1):
        seqFib.append(seqFib[len(seqFib)-1]+seqFib[len(seqFib)-2])

    for i in range(len(seqFib)-1, -1, -1):
        if i == 0:
            print(seqFib[i])
        else:
            print(seqFib[i], end=" ")
