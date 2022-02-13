print('{:=^40}'.format(' Desafio 050 '))

soma = 0
cont = 0
num = 0
for i in range(1, 7):
    num = int(input('\nDigite {}⍛ valor: '.format(i)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('\nVocê informou {} números pares e a soma deles foi {}\n'.format(cont, soma))    
    
    