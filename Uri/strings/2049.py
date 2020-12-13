# Números de Ahmoc

inst = 1
while True:
    a = input()
    if a == '0':
        break
    nums = input()

    if inst > 1:
        print()

    print("Instancia", inst)
    if a in nums:
        print("verdadeira")
    else:
        print("falsa")

    inst += 1