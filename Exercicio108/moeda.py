def metade(num):
    n = num / 2
    return n


def dobro(num):
    n = num * 2
    return n


def aumentar(p, num):
    p /= 100
    n = num + (num * p)
    return n


def diminuir(p, num):
    p /= 100
    n = num - (num * p)
    return n


def fmoeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
