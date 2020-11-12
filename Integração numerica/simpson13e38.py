import math

# PARA SIMPSONS 1/3

def fDeX(x):
    #return math.sin(math.pow(x, 2)) * math.cos(x) * math.exp(-2*x) #EX a)
    return math.cos(math.pow(x, 2)/2) + math.pow(x, 2) * math.sin(x)#EX b)
    #return math.exp(-x) * math.cos(math.pow(x, 3)/4) #EX c)
    #return math.cos(math.pow(x, 4)/4) * math.cos(math.pow(x, 3)/3) #EX d)


def simpson13(xizes, h):
    soma = 0
    m = 1
    for i in range(0, len(xizes)):
        if i == 0 or i == len(xizes) - 1:
            m = 1
        elif i % 2 == 0:
            m = 2
        else:
            m = 4

        fDeXVezesM = m * fDeX(xizes[i])
        soma = soma + fDeXVezesM
        print("x = {}  f(x) = {:.4f} m = {} f(x)*m = {:.4f}".format(xizes[i], fDeX(xizes[i]), m, fDeXVezesM))

    print("\nsoma = {:.4f}".format(soma))
    return (h/3)*soma

def simpson38(xizes, h):
    soma = 0
    m = 1
    for i in range(0, len(xizes)):
        if i == 0 or i == len(xizes) - 1:
            m = 1
        elif (i+1) % 4 == 0:
            m = 2
        else:
            m = 3

        fDeXVezesM = m * fDeX(xizes[i])
        soma = soma + fDeXVezesM
        print("x = {}  f(x) = {:.4f} m = {} f(x)*m = {:.4f}".format(xizes[i], fDeX(xizes[i]), m, fDeXVezesM))

    print("\nsoma = {:.4f}".format(soma))
    return (3*h/8)*soma


xizes = [0, 0.5, 1, 1.5, 2, 2.5, 3]
xizes = [-2, -1.5, -1, -0.5, 0, 0.5, 1]
xizes = [0, 0.4, 0.8, 1.2, 1.6, 2, 2.4]
xizes = [-1, -0.5, 0, 0.5, 1, 1.5, 2]

N = 6
h = (xizes[len(xizes)-1] - xizes[0])/N
print("h = {}\n".format(h))

print("Simpson 1/3 = {:.4f}".format(simpson13(xizes, h)))
#print("Simpson 3/8 = {:.4f}".format(simpson38(xizes, h)))

