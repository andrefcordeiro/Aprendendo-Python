# A Volta do Radar

while True:
    t = int(input())

    if t == 0:
        break

    for i in range(0, t):
        n = int(input())

        if (n - 1) % 2 == 0: # se há apenas 1 na ponta
            print(2*(n-1) + 1)

        else: # se as 2 pontas estão ocupadas
            print(2 * (n - 2) + 2)
