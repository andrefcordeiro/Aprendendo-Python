# Array Hash

n = int(input())

for i in range(0, n):
    l = int(input())
    hash = 0

    elem = 0
    pos = 0

    for j in range(0, l):
        string = input()

        for c in range(0, len(string)):
            hash += ord(string[c]) - 65 + elem + pos
            pos += 1

        elem += 1
        pos = 0

    print(hash)