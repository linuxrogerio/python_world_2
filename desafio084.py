print('{:=^40}'.format(' Desafio 084 '))

pessoa = []
pessoas = []

maior = menor = cont = 0

while True:
    pessoa.append(str(input('Digite o nome: ')))
    pessoa.append(int(input('Digite o peso: ')))
    pessoas.append(pessoa[:])
        
    if cont == 0:
        maior = menor = pessoa[1]
    elif pessoa[1] > maior:
        maior = pessoa[1]
    elif pessoa[1] < menor:
        menor = pessoa[1]
        
    pessoa.clear()
    cont += 1
    opcao = str(input('Quer continuar? [S/N] ')).strip().lower()
    
    if opcao == 'n':
        break
    
print(pessoas)
print(f'\nAo todo foram cadastradas {len(pessoas)} pessoas!')
print(f'O maior peso foi {maior}Kg')