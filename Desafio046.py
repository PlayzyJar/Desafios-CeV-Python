from time import sleep
print('=-='*20, '\n', '{:^60}'.format('== Contagem Regressiva =='))
print('=-='*20)
for c in range(10, -1, -1):
    print('{}, '.format(c), end='')
    sleep(1)
print('1\n>>Feliz Ano Novo!!!')
