from Exercicio109 import moeda
n = float(input('>>Digite um valor: R$'))
print('{}=-={}'.format('\033[1;33m', '\033[m')*15)
print(f'>>A metade de {moeda.fmoeda(n)} é {moeda.metade(n, formatBR=True)}')
print(f'>>O dobro de {moeda.fmoeda(n)} é {moeda.dobro(n, formatBR=True)}')
print(f'>>Aumentando 13% de {moeda.fmoeda(n)}, temos {moeda.aumentar(13, n, formatBR=True)}')
print(f'>>Diminuindo 10% de {moeda.fmoeda(n)}, temos {moeda.diminuir(10, n, formatBR=True)}')
