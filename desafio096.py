def area(largura, comprimento):
    area = largura * comprimento
    print(f'\nA área de um terreno de {largura}X{comprimento}  é: {area}m2\n')

#Main app
print('\n---- CONTROLE DE TERRENOS ----\n')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))

area(l, c)
