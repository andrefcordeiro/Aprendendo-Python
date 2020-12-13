# Seis Strings

string = input()
k = int(input())
indice = 0
qtdDiferentesAnt = 0
qtdDifSegLinha = 0

for i in range(0, 5):
    aux = input()
    qtdDiferentes = 0
    for j in range(0, len(string)):
        if aux[j] != string[j]:
            qtdDiferentes += 1

    if qtdDiferentes < qtdDiferentesAnt or i == 0:
        indice = i

        qtdDiferentesAnt = qtdDiferentes

    if i == 0:
        qtdDifSegLinha = qtdDiferentesAnt

if qtdDiferentesAnt > k:
    print(-1)
else:
    print(indice+1)
    print(qtdDifSegLinha)