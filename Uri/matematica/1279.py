# Ano Bissexto ou Ano não Bissexto

quebraDeLinha = 0
while True:
  try:
    n = int(input())
    if quebraDeLinha == 1:
        print()
    quebraDeLinha = 1
    isOrd = 1

    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        print("This is leap year.")
        isOrd = 0

    if n % 15 == 0:
        print("This is huluculu festival year.")
        isOrd = 0

    if n % 55 == 0 and ((n % 4 == 0 and n % 100 != 0) or n % 400 == 0):
        print("This is bulukulu festival year.")

    if isOrd == 1:
        print("This is an ordinary year.")

  except EOFError:
    break