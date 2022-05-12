print('{:=^40}'.format(' Desafio 065 '))

msg = 'S'
cont = total = num = maior = menor = 0


while msg in 'sS':
    num = int(input('Digite um número: '))
    msg = str(input('Quer continuar? [S/N] ')).lower()
      
    cont += 1
    total += num
       
    if num >= maior:
        maior = num
        if num > 0 and menor > maior:
            menor = num
    
media = total / cont
    
print('\nAcabou!\n')
print(f'\nVocê digitou {cont} números e a media deles foi {media:.0f}.\n')
print(f'\nO maior valor foi {maior} e o menor foi {menor}')
