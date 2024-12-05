def metade(num, formatBR=False):
    n = num / 2
    return n if formatBR is False else fmoeda(n)


def dobro(num, formatBR=False):
    n = num * 2
    return n if formatBR is False else fmoeda(n)


def aumentar(p, num, formatBR=False):
    p /= 100
    n = num + (num * p)
    return n if formatBR is False else fmoeda(n)


def diminuir(p, num, formatBR=False):
    p /= 100
    n = num - (num * p)
    return n if formatBR is False else fmoeda(n)


def fmoeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
