def area(l, c):
    tamanho = l * c
    print(f'O tamanho do terreno é: {tamanho}m2')

#Main app
print('\n---- CONTROLE DE TERRENOS ----\n')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))

area(l, c)
