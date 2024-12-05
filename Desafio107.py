from Exercicio107 import moeda
n = int(input('>>Digite um valor: R$'))
print('{}=-={}'.format('\033[1;33m', '\033[m')*15)
print(f'>>A metade de R${n} é R${moeda.metade(n):.2f}')
print(f'>>O dobro de R${n} é R${moeda.dobro(n):.2f}')
print(f'>>Aumentando 13% de R${n}, temos R${moeda.aumentar(13, n):.2f}')
print(f'>>Diminuindo 10% de R${n}, temos R${moeda.diminuir(10, n):.2f}')
