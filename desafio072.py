print('{:=^40}'.format(' Desafio 072 '))

valor = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
         'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
         'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
         'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
posicao = 0

while True:
    posicao = int(input("Digite um número entre 0 e 20: "))
    while posicao < 0 or posicao > 20:
        print('Tente novamente. ')
        posicao = int(input("Digite um número entre 0 e 20: "))
    if posicao > 0 or posicao < 20:
        break
        
print(f'Você digitou o número {valor[posicao]}')