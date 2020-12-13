# Turma do JB6

# retorna 1 quando jogador 1 venceu, 0 caso empate, -1 caso perdeu
def vencedor(jogada1, jogada2):
    if jogada1 == "papel":
        if jogada2 == "pedra":
            return 1
        if jogada2 == "tesoura":
            return -1
        else:
            return 0

    if jogada1 == "tesoura":
        if jogada2 == "papel":
            return 1
        if jogada2 == "pedra":
            return -1
        else:
            return 0

    if jogada1 == "pedra":
        if jogada2 == "tesoura":
            return 1
        if jogada2 == "papel":
            return -1
        else:
            return 0

    else:
        print("Jogada inválida")
        return 2

while True:
    try:
        linha = input().split(" ")
        dodo = linha[0]
        leo = linha[1]
        pepper = linha[2]

        if vencedor(dodo, leo) == 1 and vencedor(dodo, pepper) == 1:
            print("Os atributos dos monstros vao ser inteligencia, sabedoria...")

        elif vencedor(leo, dodo) == 1 and vencedor(leo, pepper) == 1:
            print("Iron Maiden's gonna get you, no matter how far!")

        elif vencedor(pepper, dodo) == 1 and vencedor(pepper, leo) == 1:
            print("Urano perdeu algo muito precioso...")

        else:
            print("Putz vei, o Leo ta demorando muito pra jogar...")

    except EOFError:
        break