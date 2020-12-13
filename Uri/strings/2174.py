# Coleção de pomekon

n = int(input())
pomekons = []
cont = 151

for i in range(0, n):
    pome = input()
    if pome not in pomekons:
        pomekons.append(pome)
        cont -= 1

print("Falta(m) {} pomekon(s).".format(cont))