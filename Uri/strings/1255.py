# Frequência de Letras

n = int(input())
freq = [] #vetor que guardara a frequencia de cada uma das 26 letras
for j in range(0, 26): #iniciando com 0 cada um dos indices
    freq.append(0)


for i in range(0, n):
    for j in range(0, 26):  # iniciando com 0 cada um dos indices
        freq[j] = 0

    str = input().lower()

    for j in range(0, len(str)): #verificando a frequencia
        if 0 <= ord(str[j]) - 97 < 26:
            freq[ord(str[j]) - 97] += 1

    maior = freq[0] #guarda a maior frequencia encontrada
    for j in range(0, len(freq)):
        if(freq[j] > maior):
            maior = freq[j]

    for j in range(0, len(freq)): #encontrando e printando todos os elementos com maior frequencia
        if (freq[j] == maior):
            print(chr(97+j), end='')

    print()