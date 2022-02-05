print('########## Desafio 040 ##########')

nota1 = float(input('Insira a primeira nota do aluno: '))
nota2 = float(input('Insira a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('\nREPROVADO!\n')
elif media >= 7.0:
    print('\nAPROVADO!\n')
elif media >= 5.0 and media < 6.9:
    print('\nRECUPERAÇÃO!\n')
print(media)