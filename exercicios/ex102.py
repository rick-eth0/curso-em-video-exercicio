def fatorial(n, show=False):
    """
    -> Calculando o fatorial de um numero.
    :param n: o numero a ser calculado.
    :param show: (opcional) Mostrar ou nao a conta.
    :return: o valor do fatorial de um numero n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            if c >1:
                print(f'{c} x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f



# programa principal
#print(fatorial(5, show=True))
help(fatorial)