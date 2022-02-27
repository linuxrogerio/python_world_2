from datetime import date
print('{:=^40}'.format(' Desafio 054 '))

atual = date.today().year
maior = 0
menor = 0

"""
if idade >= 21:
    print('Essa pessoa é maior')
else:
    print('Essa pessoa é menor')"""
    
for pessoa in range(1, 8):
    nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(pessoa)))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('\nAo todo tivemos {} pessoas maiores de idade,'.format(maior))
print('E também tivemos {} pessoas menores de idade.\n'.format(menor))


    