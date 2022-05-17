print('{:=^40}'.format(' Desafio 071 '))

while True:
    valor = int(input('\nInforma o valor do saque: R$ '))
    
    opcao = ' '
    opcao = str(input('\nDeseja realizar outro saque? [S/N]')).lower().strip()[0]
    
    if opcao in 'nN':
        break
print('\nAcabou!')
    