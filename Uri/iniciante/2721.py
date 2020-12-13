# Indecisão das Renas

bol = input().split()
nomes = ["Dasher", "Dancer", "Prancer", "Vixen", "Comet", "Cupid", "Donner", "Blitzen", "Rudolph"]
soma = 0
for i in range(0, len(bol)):
    bol[i] = int(bol[i])
    soma += bol[i]

pos = 0
ultima = 0

while soma > 0:
    soma -= 1

    if pos == 8:
        pos = 0
    else:
        pos += 1

print(nomes[pos-1])