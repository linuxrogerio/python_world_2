def aumentar(preço=0, taxa=0, formato=False):
    valor = preço + (preço * taxa / 100)
    return valor if formato is False else moeda(valor)


def diminuir(preço=0, taxa=0, formato=False):
    valor = preço - (preço * taxa / 100)
    return valor if formato is False else moeda(valor)


def dobro(preço=0, formato=False):
    valor = preço * 2
    return valor if not formato else moeda(valor)


def metade(preço=0, formato=False):
    valor = preço / 2
    return valor if not formato else moeda(valor)


def moeda(preço=0, moeda='R$'):
    return f'{moeda} {preço:>.2f}'.replace('.',',')
