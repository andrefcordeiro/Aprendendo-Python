# Aliteração

while True:
  try:
    char = []
    qtd = 0
    seq = 0
    str = input().lower().split(" ")
    charAnt = str[0][0]

    for i in range(1, len(str)):
        char = str[i][0]
        if char == charAnt and seq == 0:
          qtd += 1
          seq = 1
        elif char != charAnt:
          seq = 0
        charAnt = char

    print(qtd)

  except EOFError:
    break