def aumentar(preço=0, taxa=0, formato=False):
    '''
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preço: O preço que se quer reajustar
    :param taxa: Qual é a porcentagem do aumento
    :param formato: Quer a saída formatada ou não?
    :return: O valor reajustado, com ou sem formato.
    '''
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


def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço informado: \t{moeda(preço)}')
    print(f'Dobro desse preço é: \t{dobro(preço, True)}')
    print(f'Metade desse preço é: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento; \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-' * 30)