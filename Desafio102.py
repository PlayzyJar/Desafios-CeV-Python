def fatorial(num, show=True):
    """
    >>Calcula o fatorial de um número.
    :param num: Número a ser calculado;
    :param show: (opcional) Mostrar/Não mostrar a conta;
    :return: O valor Fatorial de um número num.
    """
    print(f'>>Calculando fatorial de {num}! = ', end='')
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end='')
            print(' x ' if c > 1 else ' = ', end='')
        f *= c
    return f


print(fatorial(5, show=False))
