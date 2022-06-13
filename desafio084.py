print('{:=^40}'.format(' Desafio 084 '))

pessoa = []
pessoas = []

maior = menor = 0

while True:
    pessoa.append(str(input('Digite o nome: ')))
    pessoa.append(float(input('Digite o peso: ')))
    if len(pessoas) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear()
           
    opcao = str(input('Quer continuar? [S/N] ')).strip().lower()
    
    if opcao == 'n':
        break
    
print('-=' * 30)
print(f'\nAo todo foram cadastradas {len(pessoas)} pessoas!')
print(f'\nO maior peso foi {maior:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi {menor:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()
print('-=' * 30)