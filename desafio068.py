from random import randint
print('{:=^40}'.format(' Desafio 068 '))





ganhou = 'S'

while ganhou in 'sS':
    #gerando o número do computador
jogada_compudator = randint(1,2)
    
    opcao = str(input("Digite 'P' para PAR e 'I' para Ímpar:"))
    if opcao in 'pP':
        jogada = 2
    else:
        jogada = 1
        
    if jogada == jogada_compudator:
        print('Jogo empatado!')
        ganhou = 's'