cores = {'amarelo': '\033[1;33m',
         'anil': '\033[1;36m',
         'negrito': '\033[1m',
         'clean': '\033[m'}
print('{}=-={}'.format(cores['amarelo'], cores['clean'])*21)
print('{:^73}'.format('{}== GERADOR DE PA =={}'.format(cores['anil'], cores['clean'])))
print('{}=-={}'.format(cores['amarelo'], cores['clean'])*21)
t = int(input('{}>>Digite o primeiro termo: '.format(cores['negrito'])))
r = int(input('>>Razão: '))
c = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while c <= total:
        print('{}'.format(t), end='')
        print(' > ' if c <= total-1 else '', end='')
        c += 1
        t += r
    mais = int(input('\n>>PAUSA!\n>>Você deseja ver mais quantos termos? '))
print('>>Fim da Progressão com {} termos mostrados.'.format(total))
