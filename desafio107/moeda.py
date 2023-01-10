def aumentar(preço, taxa):
    valor = preço + (preço * taxa / 100)
    return valor


def diminuir(preço, taxa):
    valor = preço - (preço * taxa / 100)
    return valor


def dobro(preço):
    valor = preço * 2
    return valor


def metade(preço):
    valor = preço / 2
    return valor
