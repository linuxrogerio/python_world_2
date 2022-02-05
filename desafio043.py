print('########## Desafio 043 ##########')

peso = float(input('\nInforme o peso de uma pessoa: '))
altura = float(input('\nInforme a altura dessa pessoa: '))

imc = peso / (altura ** 2)

print('IMC: {}'.format(imc))

if imc < 18.5:
    print('\nAbaixo do peso.')
elif imc >= 18.5 and imc  < 25:
    print('\nPeso Ideal.')
elif imc >= 25 and imc < 30:
    print('\nSobrepeso.')
elif imc >= 30 and imc < 40:
    print('\nObesidade.')
elif imc >= 40:
    print('\nObesidade mórbida.')