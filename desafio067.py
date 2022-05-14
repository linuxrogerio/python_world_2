print('{:=^40}'.format(' Desafio 067 '))

n = 0
#cont = 1 

while True:
    cont = 1
    n = int(input('\nQuer ver a tabuada de qual valor? '))
    if n < 0:
        break
    else:
        while cont <=10:
            print(f'{n} x {cont} = {n * cont}')
            cont += 1

print('\nTABUADA ENCERRADA!')