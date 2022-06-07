print('{:=^40}'.format(' Desafio 075 '))


valores = (int(input('Digite um número: ')), 
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')), 
         int(input('Digite o último número: ')))
print(f'\nVocê digitou os valores {valores}')
print(f'\nO valor 9 apareceu {valores.count(9)} vez(es).')
if 3 in valores:
    print(f'\nO número 3 foi digitado na {valores.index(3)+1}° posição.')
else:
    print('\nO valor 3 não foi digitado em nenhuma posição.')
print('\nOs valores pares digitados foram: ', end='')

for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
        


