import math

#AQUI VAI A f(x)
def fDeX(x):
    #return math.sin(math.pow(x, 2)) * math.cos(x) * math.exp(-2*x) #EX a)
    #return math.cos(math.pow(x, 2)/2) + math.pow(x, 2) * math.sin(x)#EX b)
    #return math.exp(-x) * math.cos(math.pow(x, 3)/4) #EX c)
    return math.cos(math.pow(x, 4) / 4) * math.cos(math.pow(x, 3) / 3)  # EX d)

#AQUI É FEITA O CÁLCULO DA QUADRATURA, RETORNANDO ORESULTADO DA INTEGRAL
def quadraturaGauss(UIs, WIs, a, b):
    soma = 0

    for i in range(0, len(UIs)):
        ri = ((b - a) / 2) * UIs[i] + ((b + a) / 2)
        fDeRiVezesWi = fDeX(ri) * WIs[i]
        soma = soma + fDeRiVezesWi
        print("ri = {:.4f}  f(ri) = {:.4f}   f(ri)*WIs = {:.4f}".format(ri, fDeX(ri), fDeRiVezesWi))

    print("\nsoma = {:.4f}".format(soma))
    return ((b - a)/2)*soma

#QUANTIDADE DE PARTIÇÕES
N = 6

if N == 4:# para n = 4
    UIs = [-0.861136, -0.339981, 0.339981, 0.861136]
    WIs = [0.347855, 0.652145, 0.652145, 0.347855]

elif N == 6: #para n = 6
    UIs = [-0.932470, -0.661209, -0.238619, 0.238619, 0.661209, 0.932470]
    WIs = [0.171324, 0.360762, 0.467914, 0.467914, 0.360762, 0.171324]

#LIMITES INFERIOR (a) E SUPERIOR (b)
limInf = -1
limSup = 2

print("Para N = {}".format(N))
print("RESULTADO DA INTEGRAL = {:.4f}".format(quadraturaGauss(UIs, WIs, limInf, limSup)))
