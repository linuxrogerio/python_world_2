import moeda

valor = float(input('Digite o preço: R$ '))

print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'Aumentado em 10%, temos  {moeda.moeda(moeda.aumentar(valor, 10))}')
print(f'Reduzido em 10%, temos  {moeda.moeda(moeda.diminuir(valor, 10))}')
