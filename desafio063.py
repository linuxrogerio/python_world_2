print('{:=^40}'.format(' Desafio 063 '))

termos = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1

print('~'*40)
print('\nSequência de Fibonacci.\n')
print(f'{t1} -> {t2}', end='')

cont = 3

#import pdb;pdb.set_trace() #debugging
while cont <= termos:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
print('~'*30)    
    