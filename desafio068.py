from random import randint
print('{:=^40}'.format(' Desafio 068 '))


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
        print('\nvocê venceu!!! FIM DO PROGRAMA.')
        break
    else:
        print('\nO computador Venceu!! TENTE NOVAMENTE...')
        

