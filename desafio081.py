print('{:=^40}'.format(' Desafio 081 '))

cont = 0
lista = []

while True:
    lista.append(int(input('\nDigite um valor: ')))
    opcao = str(input('\nQuer continuar? [S/N]')).strip().lower()
        
    if opcao in 'n':
        break
    
print('-=' * 30)
print(f'\nForam digitados {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'\nOs valores em ordem decrescente são: {lista}.')
if 5 in lista:
    print(f'\nO valor 5 faz parte da lista!')
else:
    print('\nO valor 5 não foi encontrado na lista!')

    
      
    