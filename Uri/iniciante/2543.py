# Jogatina UFPR

while True:
    try:
        string = input().split(" ")
        n = int(string[0])
        id = int(string[1])
        cont = 0

        for c in range(0, n):
            string = input().split(" ")
            i = int(string[0])
            j = int(string[1])

            if i == id and j == 0:
                cont += 1

        print(cont)

    except EOFError:
        break