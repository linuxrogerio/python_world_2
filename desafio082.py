print('{:=^40}'.format(' Desafio 082 '))

lista = []
pares = []
impares = []

while True:
    lista.append(int(input('\nDigite um valor: ')))
    if lista[-1] % 2 == 0:
        pares.append(lista[-1])
        print('\né par')
    else:
        impares.append(lista[-1])
    
    opcao = str(input('\nDeseja continuar? [S/N]: ')).strip().lower()
    if opcao == 'n':
        break
print('-=' * 30)
print(f'\nA lista completa é: {lista}')
print(f'\nA lista de pares é: {pares}')
print(f'\nA lista de ímpares é: {impares}')
print('-=' * 30)