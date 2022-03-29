print('{:=^40}'.format(' Desafio 060 '))

num = int(input('\nInforme um número: '))
fat = num
digitado = num

while num > 1:
    print(num * (num - 1))
    fat = fat * (num -1)
    num -= 1
print(f'\nO fatorial de {digitado} é: {fat}')