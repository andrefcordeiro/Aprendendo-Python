# Relógio Antigo

while True:
  try:
    str = input().lower().split(" ")
    h = int(str[0])
    m = int(str[1])

    if h/30 < 10:
        print("0{:.0f}:".format(h/30), end="")
    else:
        print("{:.0f}:".format(h/30), end="")

    if m/6 < 10:
        print("0{:.0f}".format(m/6))
    else:
        print("{:.0f}".format(m / 6))

  except EOFError:
    break