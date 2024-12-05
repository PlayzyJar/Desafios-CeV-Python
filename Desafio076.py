lista = ('Lápis', 1.75, 'Borracha', 2.0, 'Caderno', 15.9, 'Estojo', 25,
         'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32,
         'Canetas', 22.3, 'Livro', 34.9)
print('{}=-='.format('\033[1m')*25)
print('{:^75}'.format('== LISTA DE PREÇOS =='))
print('=-='*25)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<66}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
