from random import randint
from time import sleep

print('{:=^40}'.format(' Desafio 045 '))

itens = ('Pedra', 'Papel', 'Tesoura')

menu = """\njogador um dos ítems para jogarmos:

0 -> Pedra 
1 -> Papel
2 -> Tesoura

"""
print(menu)
jogador = int(input('\njogador umas das opções acima, digitando o número correspondente: '))

#Sorteando a jogador da máquina...
computador = randint(0, 2)

print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=' * 11)
print('\nVocê escolheu {}'.format(itens[jogador]))
print('\nA máquina escolheu {}'.format(itens[computador]))
print('=-' * 11)

if computador == 0: #Computador jogou Pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: #Computador jogou Papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: #Computador jogou Tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
