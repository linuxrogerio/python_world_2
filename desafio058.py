print('{:=^40}'.format(' Desafio 058 '))

from random import randint

r = randint(0, 10)
palpite = 1
chamada = """\n
Olá! Sou seu computador\n
Acabei de pensar em um número entre 0 e 10.
\nTente adivinhar que número é esse: """

user_num = int(input(chamada))

while user_num != r:
    palpite += 1
    if user_num > r:
        user_num = int(input('Menos.. tente novamente: '))
    else:
        user_num = int(input('Mais.. tente novamente: '))
    

print(f'\nVocê ACERTOU! seu palpite foi {user_num} e o numero que a máquina escolheu também foi {r}.')
print(f'\nVocê tentou {palpite} vezes até acertar!')
