# A última criança boa

nomes = []
while True:
    try:
        nome = input()
        nomes.append(nome)

    except EOFError:
        nomes.sort(key=str.lower)
        print(nomes[len(nomes)-1])
        break
