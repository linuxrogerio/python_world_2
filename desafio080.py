print('{:=^40}'.format(' Desafio 080 '))

lista = []

for i in range(0, 5):
    num = int(input('\nDigite um valor: '))
    if i == 0 or num > lista[-1]:
        lista.append(num)
        print('\nAdicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'\nAdicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'\nOs valores digitados em ordem foram {lista}')