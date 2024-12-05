print('=-='*24, '\n', '{:^69}'.format('== 10 TERMOS de uma P.A. =='))
print('=-='*24)
num = int(input('>>Digite o primeiro termo: '))
r = int(input('>>Razão: '))
decimo = num + (10 - 1) * r
for n in range(num, decimo+1, r):
    print('{} -> '.format(n), end='')
print('Fim da P.A.!')
