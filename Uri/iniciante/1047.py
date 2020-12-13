# Tempo de Jogo com Minutos

line = input().split(" ")
hi = int(line[0])
mi = int(line[1])
hf = int(line[2])
mf = int(line[3])
h = []
m = []

if hi == hf and mf > mi:
    h = 0


elif hf > hi:
    h = hf - hi

else:
    h = 24 - (hi - hf)

if mf >= mi:
    m = mf - mi

else:
    m = 60 - (mi - mf)
    h -= 1

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h, m))