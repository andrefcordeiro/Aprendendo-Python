# Brinquedos do papai noel

n = int(input())
car = 0
bon = 0

for i in range(0, n):
    linha = input().split()
    gen = linha[1]

    if gen == 'F':
        bon += 1
    else:
        car += 1

print(car, "carrinhos")
print(bon, "bonecas")
