# Mais cavalos

string = input().split(" ")
ini = string[0]
fim = string[1]
colIni = ord(ini[0])
linIni = int(ini[1])
colFim = ord(fim[0])
linFim = int(fim[1])

if colIni - 2 <= colFim <= colIni + 2 and colFim != colIni and linIni - 2 <= linFim <= linIni + 2 and linFim != linIni:
    # diagonais
    if (colFim == colIni+2 and linFim == linIni+2) or (colFim == colIni+2 and linFim == linIni-2) or (colFim == colIni-2 and linFim == linIni+2) or (colFim == colIni-2 and linFim == linIni-2):
        print("INVALIDO")
    elif (colFim == colIni-1 and linFim == linIni-1) or (colFim == colIni+1 and linFim == linIni+1) or (colFim == colIni-1 and linFim == linIni+1) or (colFim == colIni-1 and linFim == linIni-1):
        print("INVALIDO")
    else:
        print("VALIDO")
else:
    print("INVALIDO")