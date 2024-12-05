from Exercicio108 import moeda
n = float(input('>>Digite um valor: R$'))
print('{}=-={}'.format('\033[1;33m', '\033[m')*15)
print(f'>>A metade de {moeda.fmoeda(n)} é {moeda.fmoeda(moeda.metade(n))}')
print(f'>>O dobro de {moeda.fmoeda(n)} é {moeda.fmoeda(moeda.dobro(n))}')
print(f'>>Aumentando 13% de {moeda.fmoeda(n)}, temos {moeda.fmoeda(moeda.aumentar(13, n))}')
print(f'>>Diminuindo 10% de {moeda.fmoeda(n)}, temos {moeda.fmoeda(moeda.diminuir(10, n))}')
