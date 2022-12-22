from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    print('-=' * 20)
    print(f'\nContagem de {inicio} até {fim} de {passo} em {passo}:')
    sleep(2.5)


    if inicio < fim:
        for num in range(inicio, fim+1, passo):
            print(f'{num} ', end='', flush=True)
            sleep(0.5)
        print("FIM!")
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM!')

#Main App
contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 20)
print('Agora é usa vez de personalizar a contagem!')
ini = int(input('Início:   '))
fim = int(input('Fim:      '))
pas = int(input('Passo:    '))

contador(ini, fim, pas)