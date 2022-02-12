print('{:=^40}'.format(' Desafio 048 '))
soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        cont += 1
print('\nA soma dos {} valores solicitados é {}.\n'.format(cont, soma))
