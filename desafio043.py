print('########## Desafio 043 ##########')

peso = float(input('\nInforme o peso de uma pessoa: (KG): '))
altura = float(input('\nInforme a altura dessa pessoa: '))

imc = peso / (altura ** 2)

print('\nO IMC dessa pessoa é: {:.1f}'.format(imc))

if imc < 18.5:
    print('\nAbaixo do peso.\n')
elif  18.5 <= imc  < 25:
    print('\nPeso Ideal.\n')
elif 25 <= imc < 30:
    print('\nSobrepeso.\n')
elif 30 <= imc < 40:
    print('\nObesidade.\n')
elif imc >= 40:
    print('\nObesidade mórbida.\n')
