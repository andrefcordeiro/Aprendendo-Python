# Rodizio veícular

n = int(input())

for i in range(0, n):
    placa = input()

    if len(placa) != 8 or placa[3] != "-":
        print("FAILURE")

    else:
        fail = False

        for j in range(0, len(placa)):
            if j < 3: #analisando as letras
                if 65 > ord(placa[j]) or ord(placa[j]) > 90:
                    fail = True
                    break

            elif j >= 4: #analisando os numeros
                if 48 > ord(placa[j]) or ord(placa[j]) > 57:
                    fail = True
                    break

        if fail is True:
            print("FAILURE")

        else:
            # decidindo os dias da semana
            if placa[len(placa)-1] == "1" or placa[len(placa)-1] == "2":
                print("MONDAY")
            elif placa[len(placa)-1] == "3" or placa[len(placa)-1] == "4":
                print("TUESDAY")
            elif placa[len(placa)-1] == "5" or placa[len(placa)-1] == "6":
                print("WEDNESDAY")
            elif placa[len(placa)-1] == "7" or placa[len(placa)-1] == "8":
                print("THURSDAY")
            elif placa[len(placa)-1] == "9" or placa[len(placa)-1] == "0":
                print("FRIDAY")

