# Pedra-papel-tesoura-lagarto-Spock

# retorna 1 quando jogador 1 venceu, 0 caso empate, -1 caso perdeu
def vencedor(jogada1, jogada2):
    if jogada1 == "papel":
        if jogada2 == "pedra" or jogada2 == "spock":
            return 1
        if jogada2 == "lagarto" or jogada2 == "tesoura":
            return -1
        else:
            return 0

    if jogada1 == "tesoura":
        if jogada2 == "papel" or jogada2 == "lagarto":
            return 1
        if jogada2 == "pedra" or jogada2 == "spock":
            return -1
        else:
            return 0

    if jogada1 == "pedra":
        if jogada2 == "tesoura" or jogada2 == "lagarto":
            return 1
        if jogada2 == "spock" or jogada2 == "papel":
            return -1
        else:
            return 0

    if jogada1 == "lagarto":
        if jogada2 == "spock" or jogada2 == "papel":
            return 1
        if jogada2 == "tesoura" or jogada2 == "pedra":
            return -1
        else:
            return 0

    if jogada1 == "spock":
        if jogada2 == "tesoura" or jogada2 == "pedra":
            return 1
        if jogada2 == "papel" or jogada2 == "lagarto":
            return -1
        else:
            return 0

    else:
        print("Jogada inválida")
        return 2


n = int(input())

for i in range(0, n):
    linha = input().split()
    r = linha[0]
    s = linha[1]
    v = vencedor(r, s)

    if v == 1:
        print("rajesh")
    elif v == -1:
        print("sheldon")
    else:
        print("empate")