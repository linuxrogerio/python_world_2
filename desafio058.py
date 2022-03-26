print('{:=^40}'.format(' Desafio 058 '))

from random import randint

r = randint(0, 5)

user_num = int(input('\nO computador pensou em um número tente adivinha que número é esse: '))

print(user_num, '--', r)

