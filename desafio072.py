print('{:=^40}'.format(' Desafio 072 '))

valor = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
         'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
         'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
         'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
posicao = 0

while True:
    posicao = int(input("\nDigite um número entre 0 e 20: "))
    if 0 < posicao < 20:
        break
    print('\nTente novamente. ')
        
print(f'\nVocê digitou o número {valor[posicao]}')