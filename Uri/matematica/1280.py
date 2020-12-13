# Amigos

def pagaQuanto(m, n): #quanto jose (m) deve pagar
    if m == 0:
        return n+1

    elif n == 0 and m >= 1:
        return pagaQuanto(m-1, 1)

    elif m <= 3:
        return 200

    elif m == 4:
        return 2

    elif n >= 0 and m >= 0:
        return pagaQuanto(m - 1, pagaQuanto(m, n-1))


qtd = int(input())

for i in range(0, qtd):
    str = input().split(" ")
    jose = int(str[0]) #josé
    joao = int(str[1]) #joão
    pagamento = 0

    if jose == 0:
        pagamento = joao+1









