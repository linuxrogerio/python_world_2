def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO! por favor, digite um número inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO! por favor, digite um número real válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


#Main App
n1 = leiaInt('Digite um número Inteiro: ')
n2 = leiaFloat('Digite um número Real: ')
print(f'O inteiro digitado foi {n1} e o real foi {n2}.')
