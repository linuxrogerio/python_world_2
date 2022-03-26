print('{:=^40}'.format(' Desafio 058 '))

from random import randint

r = randint(0, 10)
palpite = 1
chamada = '\nO computador pensou em um número entre 0 e 10 tente adivinha que número é esse: '
user_num = int(input(chamada))

while user_num != r:
    print('\nVocê ERROU! tente novamente: ')
    palpite += 1
    user_num = int(input(chamada))

print(f'\nVocê ACERTOU! seu palpite foi {user_num} e o numero que a máquina escolheu também foi {r}.')
print(f'\nVocê tentou {palpite} vezes até acertar!')



