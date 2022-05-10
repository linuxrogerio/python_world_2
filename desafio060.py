#from math import factorial
#num = int(input('\nInforme um número: '))
#fat = factorial(num)
#print(f'O fatorial de {num} é {fat}.')

print('{:=^40}'.format(' Desafio 060 '))

num = int(input('\nInforme um número: '))
cont = num
f = 1

print(f'\nCalculando {num}!   - ', end='')

while cont > 0:
    print('{} '.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f *= cont
    cont -= 1


print(f)
