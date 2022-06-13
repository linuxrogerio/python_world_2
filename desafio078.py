print('{:=^40}'.format(' Desafio 078 '))

#Faca um programa que leia 5 valores numericos e gurde em uma lista
#No final, mostre qual foi o maior e o menor valor digitado.
#e a suas respectivas posiçoes na lista.
valores = []
maior = menor = 0

for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]

print('-=' * 30)
print(f'\nVocê digitou os valores {valores}')
print(f'\nO menor valor digitado foi: {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')
print() 
print(f'\nO maior valor digitado foi: {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print()
