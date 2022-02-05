print ('=========== DESAFIO 035 ===========')

r1 = int(input('\nDigite o primeiro segmento: '))
r2 = int(input('\nDigite o Segundo segmento: '))
r3 = int(input('\nDigite o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\nPode formar um triângulo.', end='')
    if r1 != r2 != r3 != r1:
        print('Triangulo ESCALENO.\n')
    elif r1 == r2 == r3:
        print('Triangulo EQUILÁTERO.\n')
    else:
        print('Triangulo ISÓSCELES.')
else:
    print('Não pode formar um triângulo.')    