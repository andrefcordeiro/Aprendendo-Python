# Abracadabra

while True:
    try:
        word = input()

        for i in range(0, len(word)):
            print(" "*i, end="")
            for c in range(0, len(word)-i):
                if c == len(word) - i - 1:
                    print(word[c])
                else:
                    print(word[c], end=" ")
        print()

    except EOFError:
        break