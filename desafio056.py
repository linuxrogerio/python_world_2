print('{:=^40}'.format(' Desafio 056 '))

soma_idade = 0
velho = 0
nova = 0

for pessoas in range(1,5):
    print('----- {}º PESSOA -----'.format(pessoas))
    nome = str(input('\nNome: ')).strip()
    idade = int(input('\nIdade: '))
    sexo = str(input('\nSexo [M/F]: ')).strip()
    sexo = sexo.upper()
    soma_idade += idade
    
    
media_idade = soma_idade / 4
print('A media de idade do grupo é de {} anos.'.format(media_idade))
  