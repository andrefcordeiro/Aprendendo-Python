def le_pol(n):
    a = []

    for i in range(n, -1, -1):
        print("Informe o a[", i, "] = ")
        val = float(input())
        a.append(val)
    return a


def le_raizes(n):

    r = []

    for i in range(n):
        print("Informe a {}ª raiz".format(i+1))
        val = float(input())
        r.append(-1 * val)  # multiplica a raiz por -1 para a utilização na fórmula

    return r


def print_pol(p):

    print("\nPolinômio: ")
    for i in range(len(p)):
        if p[i] < 0:
            print("- {}".format(-p[i]), end='')
        else:
            print("+ {}".format(p[i]), end='')
        print("x^{}".format(len(p)-1-i), end=' ')


def ger_pol(r):
    p = []
    p_aux = []
    ant = []

    if len(r) == 1: # se houver apenas 1 raiz
        ant = [1, r[0]]

        return ant

    #faz a 1ª multiplicação  (x - r1) * (x - r2)
    ant = [1, r[0] + r[1], r[0] * r[1]]

    if len(r) < 2: # se houver apenas 2 raizes
        return ant

    else:
        for i in range(2, len(r)):  # executa todas as multiplicações
            p_aux = []
            for j in range(len(ant)):
                p_aux.append(ant[j]*1)
                p_aux.append(ant[j]*r[i])

            c = 0
            ant = []
            while c < len(p_aux):  # fazendo as somas dos termos semelhantes (de mesma potência)
                if c != 0 and c != len(p_aux)-1:
                    ant.append(p_aux[c] + p_aux[c + 1])
                    c = c+2
                else:
                    ant.append(p_aux[c])
                    c = c+1

            #print(ant)

        for c in range(len(ant)):
            p.append(ant[c])

        return p



print("Quantidade de raízes: ")
n = int(input())
r = le_raizes(n)
p = ger_pol(r)

print_pol(p)

