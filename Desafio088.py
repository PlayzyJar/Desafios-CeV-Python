from time import sleep
from random import randint
jogos = []
cont = 0
cores = {'negrito': '\033[1m',
         'amarelo': '\033[1;33m',
         'anil': '\033[36m',
         'clear': '\033[m'}
print('{}=-={}'.format('\033[1;33m', '\033[m')*20)
print('{:^68}'.format('{}== JOGO MEGASSENA =={}'.format(cores['anil'], cores['clear'])))
print('{}=-={}'.format('\033[1;33m', '\033[m')*20)
res = int(input('>>Quantos jogos você quer que eu sorteie? '))
print('>>SORTEANDO', end='')
sleep(0.5)
for p in range(0, 3):
    print('.', end='')
    sleep(0.5)
for c in range(0, res):
    print('\n>>Jogo {:0>2}:'.format(c+1), end='')
    while cont < 7:
        num = (randint(1, 60))
        if num not in jogos:
            jogos.append(num)
            cont += 1
    jogos.sort()
    for n in range(0, 6):
        print(' {}[{}{:0>2}{}]{}'.format(cores['amarelo'], cores['clear'], jogos[n], cores['amarelo'], cores['clear']), end='')
    sleep(0.5)
    jogos.clear()
    cont = 0
print()
print('{}-{}'.format(cores['amarelo'], cores['clear'])*21, end='')
print(' {}>> BOA SORTE! <<{} '.format(cores['anil'], cores['clear']), end='')
print('{}-{}'.format(cores['amarelo'], cores['clear'])*21, end='')
