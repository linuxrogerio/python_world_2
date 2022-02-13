print('{:=^40}'.format(' Desafio 049 '))
num = int(input('\nDigite um número para ver sua tabuada: '))


for i in range(0, 11):
    print('{} X {:2} = {}'.format(i, num, i * num))
    