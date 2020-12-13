# Tempo do Duende

n = int(input())
linha = input().split()
a = int(linha[0])
b = int(linha[1])

if a + b > n:
    print("Deixa para amanha!")
else:
    print("Farei hoje!")