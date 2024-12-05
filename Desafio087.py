matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maior = par = totc = 0
print('{}=-={}'.format('\033[36m', '\033[m')*18)
print('{:^55}'.format('== GERADOR DE MATRIZES 3x3 =='))
print('{}=-={}'.format('\033[36m', '\033[m')*18)
for linha in range(0, 3):
    for c in range(0, 3):
        matriz[linha][c] = (int(input(f'>>Digite um valor para a posição [{linha+1}, {c+1}]: ')))
        if matriz[linha][c] % 2 == 0:
            par += matriz[linha][c]
        if c == 2:
            totc += matriz[linha][c]
        if linha == 1 and c == 0:
            maior = matriz[linha][c]
        elif linha == 1 and matriz[linha][c] > maior:
            maior = matriz[linha][c]
for linha in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[linha][c]:^5}]', end='')
    print()
print('{}=-={}'.format('\033[36m', '\033[m')*18)
print(f'>>A soma dos valores PARES digitados é igual a {par}')
print(f'>>A soma dos valores da terceira coluna é {totc}')
print(f'>>O maior valor da segunda linha é igual a {maior}')
