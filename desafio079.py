print('{:=^40}'.format(' Desafio 079 '))

lista = []

while True:
    cont = 0
    valor = int(input('\nDigite um valor: '))
    if valor in lista:
        print('\nValor duplicado! Não vou adicionar.')
    else:
        lista.append(valor)
        print('\nValor adicionado com sucesso...')
    
    opcao = 's'
    
    opcao = input('\nQuer continuar? [S/N]: ').strip().lower()
    
    if opcao in 'nN':
        break
print('-=' * 30)
lista.sort()
print(f'\nVocê digitou os valores {lista}')