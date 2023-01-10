def aumentar(preço=0, taxa=0):
    valor = preço + (preço * taxa / 100)
    return valor


def diminuir(preço=0, taxa=0):
    valor = preço - (preço * taxa / 100)
    return valor


def dobro(preço=0):
    valor = preço * 2
    return valor


def metade(preço=0):
    valor = preço / 2
    return valor


def moeda(preço=0, moeda='R$'):
    return f'{moeda} {preço:>.2f}'.replace('.',',')
