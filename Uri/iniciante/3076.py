# Exercício de História

while True:
    try:
        n = input()

        if 1 <= int(n) <= 100:
            print(1)

        else:
            allZero = 1
            for i in range(len(n) - 2, len(n)):
                if int(n[i]) != 0:
                    allZero = 0

            if allZero == 1:
                print(int(n[0: len(n) - 2]))
            else:
                print(int(n[0: len(n) - 2])+1)

    except EOFError:
        break
