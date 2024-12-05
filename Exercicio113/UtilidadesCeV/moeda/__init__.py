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


def moedaresumo(preco=0, taxaup=10, taxadown=5):
    titulo('>>RESUMO DO VALOR<<')
    print(f' >>Preço analisado: \t{fmoeda(preco)}')
    print(f' >>Dobro do preço: \t\t{dobro(preco, formatBR=True)}')
    print(f' >>Metade do preço: \t{metade(preco, formatBR=True)}')
    print(f' >>{taxaup}% de aumento: \t\t{aumentar(taxaup, preco, formatBR=True)}')
    print(f' >>{taxadown}% de desconto: \t{diminuir(taxadown, preco, formatBR=True)}')
    print(f'-'*35)


def titulo(msg):
    print('-'*35)
    print(f'{msg:^35}')
    print('-'*35)
