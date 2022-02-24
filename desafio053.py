from posixpath import split


print('{:=^40}'.format(' Desafio 053 '))

frase = str(input('\nDigite uma frase: ')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

inverso = junto[::-1]

"""for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]"""

print('\nO inverso de {} é {}'.format(junto, inverso))

if inverso == junto:
    print('\nTemos um Palíndromo!')
else:
    print('\nA frase digitada não é um Palíndromo!')