from time import sleep
print('=-='*24, '\n' '{:^72}'.format('== Contagem Par =='))
print('=-='*24)
for p in range(0, 51, 2):
    print('{} '.format(p), end='')
    sleep(0.4)
