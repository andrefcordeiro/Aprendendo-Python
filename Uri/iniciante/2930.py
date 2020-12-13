# Tcc da depressão natalino

str = input().split(" ")
entrega = int(str[0])
prazoFinal = int(str[1])

if entrega > prazoFinal:
    print("Eu odeio a professora!")

elif entrega + 3 <= prazoFinal:
    print("Muito bem! Apresenta antes do Natal!")

else:
    print("Parece o trabalho do meu filho!")

    if prazoFinal == 22:
        print("TCC Apresentado!")
    elif prazoFinal == 23:
        print("Fail! Entao eh nataaaaal!")