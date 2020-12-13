# Contando caracters

primeiro = True
maiorPalav = ""

while True:

    if primeiro is False:
        print()
    else:
        primeiro = False

    string = input()

    if string == "0":
        print("\nThe biggest word:", maiorPalav)
        break

    stringArray = string.split(" ")

    for i in range(0, len(stringArray)):
        if len(stringArray[i]) >= len(maiorPalav):
            maiorPalav = stringArray[i]

        print(len(stringArray[i]), end="")
        if i != len(stringArray) - 1:
            print("-", end="")

