print('{:=^40}'.format(' Desafio 077 '))

#Faca um programa que leia 5 valores numericos e gurde em uma lista
#No final, mostre qual foi o maior e o menor valor digitado.
#e a suas respectivas posiçoes na lista.

valores = []

for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))

print(f'\nVocê digitou os valores {valores}')