#teste = list()
#teste.append('Reis')
#teste.append(37)
#
#galera = list()
#galera.append(teste[:]) #Criando uma cópia da lista.
#
#teste[0] = 'Maria'
#teste[1] = 22
#galera.append(teste[:])
#
#print(galera)
#------------------------------------------

#galera = [['João', 19, 'M'], ['Ana', 33, 'F'], ['Joaquim', 13, 'M'], ['Maria', 45, 'F']]
#print(galera[3][2])

#for p in galera:
#    print(f'{p[0]} tem {p[1]} de idade.')

galera = list()
dado = list()
total_maior = total_menor = 0

for cont in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
    
#print(galera)

for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'\n{pessoa[0]} é maior de idade.')
        total_maior += 1
    else:
        print(f'\n{pessoa[0]} é menor de idade.')
        total_menor += 1

print(f'\nTemos {total_maior} maiores de idade e {total_menor} menores de idade.')
