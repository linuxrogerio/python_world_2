print('{:=^40}'.format(' Desafio 062 '))

primeiro = int(input('\nDigite o primeiro termo da PA: '))
razao = int(input('\nDigite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10


while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA\n')
    mais = int(input('Quantos termos você quer mostar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados')
