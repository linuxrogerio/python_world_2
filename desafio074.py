from random import randint
print('{:=^40}'.format(' Desafio 074 '))

tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

maior = menor = 0

print(f'\nOs valores sorteados foram: ', end=' ')
for i in range(0, 5):
    print(tupla[i], end=' ')
        
print(f'\nO maior número sorteado foi {max(tupla)}.')
print(f'\nO menor número sorteado foi {min(tupla)}.')
