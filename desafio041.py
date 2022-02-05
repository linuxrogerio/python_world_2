from datetime import date

atual = date.today().year

print('########## Desafio 041 ##########')

nascimento = int(input('\nInforme ano de nascimento do atleta: '))

idade = atual - nascimento

print('\nO atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('\nCategoria MIRIM.\n')
elif idade <= 14:
    print('\nCategoria INFANTIL.\n')
elif idade <= 19:
    print('\nCategoria JUNIOR.\n')
elif idade <= 25:
    print('\nCategoria SÊNIOR.\n')
else:
    print('\nCategoria MASTER.\n')