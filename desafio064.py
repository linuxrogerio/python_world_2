print('{:=^40}'.format(' Desafio 064 '))

valor = cont = total = 0

while valor != 999:
    valor = int(input('\nDigite um valor inteiro[DIGITE 999 PARA SAIR]: '))
    if valor != 999:
        total += valor
        cont +=1
    
    
print('\nAcabou!')
print(f'Foram digitados {cont} números e a soma deles é: {total}.')