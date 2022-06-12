#num = [2, 5, 9 ,1]
#num[2] = 3
#num.append(7) #Adicionando o numero 7 no fim da lista
#num.append(13) #Adicionando o numero 13 no fim da lista
#num.sort(reverse=True) #Ordenando a lista e colocando na forma reversa
#num.insert(2, 2) #inserindo o elemento 0 na posicao 2
#num.remove(2) #Removendo a primeira ocorrencia do numero 2 na lista.
#if 5 in num:
#    num.remove(5)
#else:
#    print('Não foi localizado o valor 4 na lista.')
#num.pop() #Removendo o ultimo elemento da lista
#num.pop(2) #removendo o elemento na posicao 2
#print(num)
#print(f'\nEssa lista tem {len(num)} elementos.')

valores = []
#valores.append(5)
#valores.append(9)
#valores.append(4)

for cont in range(0, 5):
    valores.append(int(input('Dgite o valor: ')))



for chave, valor in enumerate(valores):
    print(f'Na posicao {chave} eu encontrei {valor}!')
print('Cheguei ao final da lista.')    


a = [2, 3, 4, 7]
#b = a #Fazendo uma ligacao de uma lista na outra
b = a[:] #Criando uma cópia de A dentro de B

b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')