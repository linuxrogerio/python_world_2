import random
from time import sleep

print('{:=^40}'.format(' Desafio 045 '))

print('\nOlá! Eu quero jogar um jogo com você...')

menu = """\nEscolha um dos ítems para jogarmos:

1 -> Pedra 

2 -> Papel

3 -> Tesoura

"""
print(menu)
escolha = int(input('\nEscolha umas das opções acima, digitando o número correspondente: '))

#Sorteando a escolha da máquina...
escolha_maquina = random.choice(range(1, 3))


print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print(':-=40')
print('\nVocê escolheu {}'.format(escolha))
print('\nA máquina escolheu {}'.format(escolha_maquina))

if escolha == escolha_maquina:
    print('Jogo empatado')
elif escolha == 1 and escolha_maquina == 2:
    print('papel embrulha pedra - maquina ganha')
elif escolha == 1 and escolha_maquina == 3:
    print('Pedra quebra tesoura - Voce ganha')
elif escolha == 2 and escolha_maquina == 1:
    print('Papel embrulha pedra - voce ganha')
elif escolha == 2 and escolha_maquina == 3:
    print('Tesoura corta papel - maquina ganha')
elif escolha == 3 and escolha_maquina == 1:
    print('Tesoura corta papel - voce ganha')
elif escolha == 3 and escolha_maquina == 2:
    print('Papel embrulha pedra - maquina ganha')
