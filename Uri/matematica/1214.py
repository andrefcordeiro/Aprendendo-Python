# Acima da Média

c = int(input())

for i in range(0, c):
    media = 0
    string = input().split(" ")
    qtd = int(string[0])

    for j in range(1, len(string)):
        media += int(string[j])
    media = media/qtd

    acimaDaMedia = 0
    for j in range(1, len(string)):
        if int(string[j]) > media:
            acimaDaMedia += 1

    print("{:.3f}%".format((acimaDaMedia*100)/qtd))


