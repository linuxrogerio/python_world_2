print ('=========== DESAFIO 037 ===========\n')

inteiro = int(input('Digite um número inteiro: \n'))

print('Escolha a base de conversão para esse número: \n')
print('-> Digite 1 para Binário')
print('-> Digite 2 para Octal')
print('-> Digite 3 para Hexadecimal \n')

base = int(input())

print('Você escolheu {} '.format(base))

if base == 1:
    result = format(inteiro, "b")
    print('\n O valor de {} em binário é {}.'.format(inteiro, result))
elif base == 2:
    result = format(inteiro, "o")
    print('\n O valor de {} em octal é {}.'.format(inteiro, result))
elif base == 3:
    result = format(inteiro, "x")
    print('\n O valor de {} em hexadecimal é {}.'.format(inteiro, result))
else:
    print('\n Você escolheu errado, você escolher numeros entre 1 e 3.')

