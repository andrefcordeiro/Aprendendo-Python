# Validador de Senhas

while True:
    try:
        senha = input()
        inv = False #invalida
        if 6 <= len(senha) <= 32:
            hasNum = False
            hasUpp = False
            hasLow = False

            for i in range(0, len(senha)):
                if senha[i].isnumeric() and hasNum is False:
                    hasNum = True
                elif senha[i].isupper() and hasUpp is False:
                    hasUpp = True
                elif senha[i].islower() and hasLow is False:
                    hasLow = True

                if senha[i].isnumeric() is False: # se não for um número
                    if 97 > ord(senha[i].lower()) or ord(senha[i].lower()) > 122:
                        inv = True

            if hasNum is True and hasUpp is True and hasLow is True and inv is False:
                print("Senha valida.")
            else:
                print("Senha invalida.")

        else:
            print("Senha invalida.")

    except EOFError:
        break