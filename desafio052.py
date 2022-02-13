print('{:=^40}'.format(' Desafio 052 '))
tot = 0
num = int(input('Digite um número: '))
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO número {} foi divisível {} vezes.\n'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO!\n')
else:
    print('E por isso ele NÃO PRIMO!\n')
