# Dúvida Etária

nome = input()
data = input().split("/")
dataD = int(data[0])
dataM = int(data[1])
dataA = int(data[2])
aniver = input().split("/")
aniverD = int(aniver[0])
aniverM = int(aniver[1])
aniverA = int(aniver[2])

if aniverD == dataD and aniverM == dataM:
    print("Feliz aniversario!")

idade = dataA - aniverA

if aniverM > dataM or (aniverM == dataM and aniverD > dataD):
    idade -= 1

print("Voce tem {} anos {}.".format(idade, nome))