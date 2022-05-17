print('{:=^40}'.format(' Desafio 069 '))

total18 = homens = mulher_menor = 0

while True:
    idade = int(input('\nDigite a idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('\nDigite o sexo [M/F] : ')).lower().strip()[0]
    
    if sexo == 'm':
        homens += 1 
    
    if sexo == 'f' and idade < 20:
        mulher_menor += 1
    
    if idade > 18:
        total18 += 1
    
    opcao = ' '
    while opcao not in 'sn':
        opcao = str(input('\nDeseja continuar? [S/N]: ')).lower().strip()[0]
    
    if opcao == 'n':
        break
    
    
print('\nAcabou!')
print(f'\nForam cadastradas {total18} pessoas maiores de 18 anos.')
print(f'\nForam cadastrados {homens} homens no total.')
print(f'\nForam cadastradas {mulher_menor} mulheres com menos de 20 anos.\n')
