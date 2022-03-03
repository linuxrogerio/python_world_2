print('{:=^40}'.format(' Desafio 056 '))

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
total_mulher_20 = 0

for pessoas in range(1,5):
    print('----- {}º PESSOA -----'.format(pessoas))
    nome = str(input('\nNome: ')).strip()
    idade = int(input('\nIdade: '))
    sexo = str(input('\nSexo [M/F]: ')).strip()
    sexo = sexo.upper()
    soma_idade += idade
    if pessoas == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'fF' and idade < 20:
        total_mulher_20 += 1
media_idade = soma_idade / 4
print('\nA media de idade do grupo é de {} anos.'.format(media_idade))
print('\nO homem mais velho tem {} e se chama {}.'.format(maior_idade_homem, nome_mais_velho))
print('\nAo todo sāo {} mulher com menos de 20 anos.'.format(total_mulher_20))
