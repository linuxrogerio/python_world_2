print('{:=^40}'.format(' Desafio 070 '))

total = cont_produtos =  barato = cont = 0
nome_barato = ' '

while True:
    print('-='*15)
    produto = str(input('\nNome do produto: '))
    valor = float(input('\nPreço R$: '))
    cont += 1
    
    total += valor
            
    if valor > 1000:
        cont_produtos += 1
    
    if cont == 1 or valor < barato:
        barato = valor
        nome_barato = produto
    
    opcao = ' '
    while opcao not in 'sn':
        opcao = str(input('\nDeseja continuar? [S/N]: ')).lower().strip()[0]
        
    if opcao == 'n':
        break
print('\nAcabou!')
print(f'\nO total da compra foi: R$ {total:.2f}')
print(f'\nExistem {cont_produtos} produtos que custam mais que R$ 1.000,00.')
print(f'\nO produto mais barato foi {nome_barato} que custou R$ {barato:.2f}.\n')