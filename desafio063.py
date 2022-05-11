print('{:=^40}'.format(' Desafio 063 '))

termos = int(input('Quantos termos você quer mostrar? '))
cont = 0
fb = 0


while cont != termos:
    
    base =  fb 
    proximo = base + 1
    result = base + proximo
    fb = result   
    cont += 1
    print(f'{result} -> ', end='')
    