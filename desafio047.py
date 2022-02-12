

print('{:=^40}'.format(' Desafio 047 '))
soma = 0

for i in range(2, 51, 2):
    print(i, end=' ')
    soma = soma + i
        
print('\nSoma total: {}'.format(soma))