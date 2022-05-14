print('{:=^40}'.format(' Desafio 065 '))

msg = 'S'
cont = total = num = media = maior = menor = 0


while msg in 'sS':
    num = int(input('Digite um número: '))
    cont += 1
    total += num
      
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
           menor = num
    
    
    msg = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
media = total / cont
print('\nAcabou!\n')
print(f'\nVocê digitou {cont} números e a media deles foi {media:.0f}.\n')
print(f'\nO maior valor foi {maior} e o menor foi {menor}\n')
