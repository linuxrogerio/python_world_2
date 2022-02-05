print('########## Desafio 038 ##########')

n1 = int(input('Digite um número inteiro: '))
print('Numero {}'.format(n1))
n2 = int(input('Digite outro número inteiro: '))
print('Numero {}'.format(n2))

if n1 == n2:
    print('Não existe valor maior, os dois são iguais!')
elif n1 > n2:
    print('O primeiro valor é maior!')
elif n2 > n1:
    print('O segundo valor é maior!')