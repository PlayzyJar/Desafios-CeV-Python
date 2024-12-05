print('=-='*21, '\n', '{:^60}'.format('== GERADOR DE PA =='))
print('=-='*21)
t = int(input('>>Digite o primeiro termo: '))
r = int(input('>>Razão: '))
c = 1
while c <= 10:
    print('{}'.format(t), end='')
    print(' > ' if c <= 9 else '', end='')
    c += 1
    t += r
print('\n>>Fim da PA!')
