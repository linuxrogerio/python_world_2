from random import randint
print('{:=^40}'.format(' Desafio 068 '))

total_vitorias = 0

while True: 
    #Gerando o número do jogador
    opcao = str(input("\nDigite 'P' para PAR e 'I' para Ímpar: ")).lower().strip()[0]
    if opcao == 'p':
        escolha_computador = 1
        escolha_usuario = 2   
    else:
        escolha_computador = 2
        escolha_usuario = 1
            
    jogada_computador = randint(0, 10)
    jogada_usuario = int(input('\nDigite a sua jogada: '))
    
    soma = jogada_usuario + jogada_computador

    if soma % 2 == 0:
        print('\nResultado é par.')
        saida = 2
    else:
        print('\nResultado é impar.')
        saida = 1
    
    if saida == escolha_usuario:
        print('\nVocê venceu!!! VAMOS JOGAR NOVAMENTE!')
        total_vitorias += 1
    else:
        print(f'\nVocê ganhou {total_vitorias} partidas seguidas e agora perdeu! FIM DO JOGO!\n')
        break

