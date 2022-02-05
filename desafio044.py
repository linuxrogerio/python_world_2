print('########## Desafio 044 ##########')

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
    valor_final = valor - (valor * 0.10)
    print('\nO valor final a ser pago com 10% de desconto será R$ {:.2f}'.format(valor_final))
elif forma_pagamento == 2:
    valor_final = valor - (valor * 0.05)
    print('\nO valor final a ser pago com 5% de desconto será R$ {:.2f}'.format(valor_final))
elif forma_pagamento == 3:
    print('\nO valor final a ser pago será o valor original do produto R$ {:.2f}'.format(valor))
elif forma_pagamento == 4:
    valor_final = valor + (valor * 0.20)
    print('\nO valor final com 20% de juros será R$ {:.2f}'.format(valor_final))
else:
    print('\nVocê deve digitar um dos valores acima citados!')

