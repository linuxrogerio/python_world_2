from random import randint
print('{:=^40}'.format(' Desafio 074 '))

tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'\nOs valores sorteados foram: ', end=' ')
for i in tupla:
    print(i, end=' ')
        
print(f'\nO maior número sorteado foi {max(tupla)}.')
print(f'O menor número sorteado foi {min(tupla)}.')
