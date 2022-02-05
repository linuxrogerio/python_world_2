import random
import ascii


print('########## Desafio 045 ##########')

print('\nOlá! Eu quero jogar um jogo com você...')

menu = """ Escolha um dos ítems para jogarmos:

1 -> Pedra 

2 -> Papel

3 -> Tesoura

"""
print(menu)
escolha = int(input('Escolha umas das opções acima, digitando o número correspondente: '))

escolha_maquina = random.choice(range(1, 3))


print('\nSua escolha {}'.format(escolha))
print('\nEscolha da máquina {}'.format(escolha_maquina))


if 
