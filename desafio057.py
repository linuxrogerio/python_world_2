print('{:=^40}'.format(' Desafio 057 '))

sexo = str(input('\nDigite o seu sexo: [M/F]: ')).strip().upper()[0]
while sexo not in 'mMfF':
    sexo = str(input('\nDados inválidos, favor digite o seu sexo: [M/F]: ')).strip().upper()[0]
print(f'\nSexo {sexo} foi registrado com sucesso!.')
