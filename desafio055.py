print('{:=^40}'.format(' Desafio 055 '))

maior = 0
menor = 0

for pessoa in range(1, 6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso 

print('\nO maior peso digitado foi: {}Kg.'.format(maior))
print('\nO menor peso digitado foi: {}Kg.'.format(menor))
