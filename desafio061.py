print('{:=^40}'.format(' Desafio 061 '))

primeiro = int(input('\nDigite o primeiro termo da PA: '))
razao = int(input('\nDigite a razão: '))
termo = primeiro
cont = 1

while cont <=10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('FIM\n')
    