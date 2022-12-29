def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (Opcional) mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    fat = 1
    while num > 0:
        if show:
            print(num, end='')
            if num > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= num
        num -= 1
         
    return fat


#print(fatorial(5, show=False))
help(fatorial)
