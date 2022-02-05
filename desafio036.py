print ('=========== DESAFIO 036 ===========')

casa = float(input('Informe o valor da casa que deseja financiar: '))
print ('Valor {:.2f}'.format(casa))

salario = float(input('Informe o valor do salário do comprador: '))
print ('Salário R$ {:.2f}'.format(salario))

anos = int(input('Em quantos anos será realizado o financiamento? '))
print ('Financiamento em {} Anos'.format(anos))

parcela = casa / (anos * 12)
print('Com parcelas de R$ {:.2f} ao mês.'.format(parcela))

limite_salario = salario * 0.30


print ('=========== ANÁLISE DO FINANCIAMENTO ===========')

if (parcela > limite_salario ):
    print('O valor da parcela excede 30% de sua renda, Financiamento Negado!')
else:
    print('FINANCIAMENTO APROVADO COM AS CONDIÇÕES ABAIXO: ')
    print('O valor da parcela para a aquisição deste imóvel é de {:.2f} ao mếs.'.format(parcela))