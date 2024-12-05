matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for lin in range(0, 3):
    for c in range(0, 3):
        matriz[lin][c] = int(input(f'>>Digite o valor da posição [{lin}, {c}]: '))
print('{}=-={}'.format('\033[1;36m', '\033[m')*15)
for lin in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[lin][c]:^5}]', end='')
    print()
