from random import randint
print('{:=^40}'.format(' Desafio 068 '))

ganhou = 'S'

while ganhou in 'sS': 
    
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
        
    else:
        print('\nResultado é impar.')
    
        
    print(f'\nJogada computador: {jogada_computador}')
    print(f'\nJogada Jogador: {jogada_usuario}')
    print(f'\nResultado: {soma}')
    
    ganhou = 's'