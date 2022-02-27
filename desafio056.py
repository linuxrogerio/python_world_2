print('{:=^40}'.format(' Desafio 056 '))

velho = 0
nova = 0

for pessoa in range(1,5):
    nome = str(input('\nDigite o nome da {}º pessoa: '.format(pessoa)))
    idade = int(input('\nDigite a idade da {}º pessoa: '.format(pessoa)))
    sexo = str(input('\nDigite o sexo da {}º pessoa, M para masculino e F para feminino: '.format(pessoa)))
    sexo = sexo.upper()
    
    if pessoa == 1:
        if sexo == M:
            velho = nome
        else:
            nova = nome