# Reservatório de Mel

while True:
    try:
        vol = float(input())
        diam = float(input())
        r = diam/2
        h = vol/(3.14*(r**2))
        acirc = 3.14 * (r ** 2) #area do circulo ("boca")

        print("ALTURA = {:.2f}".format(h))
        print("AREA = {:.2f}".format(acirc))

    except EOFError:
        break