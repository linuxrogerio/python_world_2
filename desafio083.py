print('{:=^40}'.format(' Desafio 083 '))

expr = str(input('\nDigite a expressão: '))

pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('\nSua expressão está válida!')
else:
    print('\nSua expressaõ está errada!')
