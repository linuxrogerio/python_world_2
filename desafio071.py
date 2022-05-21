print('{:=^40}'.format(' Desafio 071 '))


valor = int(input('\nInforma o valor do saque: R$ '))
total = valor
nota = 50
contador_notas = 0

while True:
    if total >= nota:
        total -= nota
        contador_notas += 1
    else: 
        if contador_notas > 0:
            print(f'\nO total de notas de {nota} foi {contador_notas}.')
        if nota == 50:
            nota = 20
            contador_notas = 0
        elif nota == 20:
            nota = 10
            contador_notas = 0
        elif nota == 10:
            nota = 1
            contador_notas = 0
        if total == 0:
            break

