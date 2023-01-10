from desafio107 import moeda

valor = float(input('Digite o preço: R$ '))

print(f'A metade de R$ {valor} é {moeda.metade(valor)}')
print(f'O dobro de R$ {valor} é {moeda.dobro(valor)}')
print(f'Aumentado em 10%, temos R$ {moeda.aumentar(valor, 10)}')
print(f'Reduzido em 10%, temos R$ {moeda.diminuir(valor, 10)}')
