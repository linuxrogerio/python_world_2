print('{:=^40}'.format(' Desafio 044 '))

# recebendo o valor do produto
valor = float(input('\nInforme o valor do produto: '))

# criando o menu que será printado em seguida
menu = """ --------- Formas de pagamento ----------:

1 - Para pagamento à vista no dinheiro ou cheque.

2 - Para à vista no cartão.

3 - Para dividir em duas vezes no cartão.

4 - Para dividir em 3X ou mais no  cartão.

"""

print(menu)
forma_pagamento = int(input('\n Escolha uma das formas de pagamento acima: ' ))

if forma_pagamento == 1:
    valor_final = valor - (valor * 10 / 100)
    print('\nO valor final a ser pago com 10% de desconto será R$ {:.2f}'.format(valor_final))
elif forma_pagamento == 2:
    valor_final = valor - (valor * 0.05)
    print('\nO valor final a ser pago com 5% de desconto será R$ {:.2f}'.format(valor_final))
elif forma_pagamento == 3:
    valor_final = valor
    parcela = valor_final / 2
    print('\nO valor final a ser pago será R$ {:.2f} em 2X de R$ {:.2f} SEM JUROS'.format(valor, parcela))
elif forma_pagamento == 4:
    valor_final = valor + (valor * 20 / 100)
    total_parcelas = int(input('\nQuantas parcelas? '))
    parcela = valor_final / total_parcelas
    print('\nO valor final com 20% de juros será em {}X de R$ {:.2f} COM JUROS'.format(total_parcelas, parcela))
else:
    print('\nOpção inválida, você deve digitar um dos valores acima citados!')

