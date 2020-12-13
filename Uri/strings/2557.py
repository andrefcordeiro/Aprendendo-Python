# r+l=j

import re

while True:
    try:
        linha = input()
        linha = re.split('\\+', linha)
        r = linha[0]
        aux = linha[1].split("=")
        l = aux[0]
        j = aux[1]

        if r.isalpha():
            print(int(j) - int(l))

        elif l.isalpha():
            print(int(j) - int(r))

        else:
            print(int(r) + int(l))


    except EOFError:
        break