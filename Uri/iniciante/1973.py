# Jornada Nas Estrelas

n = int(input()) #não serve para nada
str = input().split(" ")
carneiros = []
totalCarneiros = 0
atacados = [0]*n

for i in range(0, len(str)):
    carneiros.append(int(str[i]))
    totalCarneiros += carneiros[i]

pos = 0
ant = 0

while True:
    if pos >= len(carneiros) or pos < 0:
        break

    ant = pos
    if carneiros[pos] % 2 != 0:
        pos += 1

    else:
        pos -= 1

    if carneiros[ant] > 0:
        carneiros[ant] -= 1
        totalCarneiros -= 1
        atacados[ant] = 1

print(atacados.count(1), totalCarneiros)
