print('{:=^40}'.format(' Desafio 059 '))

menu = """
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa\n
"""

valor1 = int(input('\nDigite o primeiro valor: '))
valor2 = int(input('\nDigite o segundo valor: '))

opcao = 0

while opcao != 5:
    opcao = int(input(menu))
    if opcao == 1:
        print(f'\nA soma de {valor1} + {valor2} = {valor1 + valor2}')
    elif opcao == 2:
        print(f'\nA multiplicação de {valor1} X {valor2} = {valor1 * valor2}')