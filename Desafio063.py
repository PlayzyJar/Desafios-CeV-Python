cores = {'amarelo': '\033[1;33m',
         'anil': '\033[1;36m',
         'negrito': '\033[1m',
         'clean': '\033[m'}
print('{}=-={}'.format(cores['amarelo'], cores['clean'])*21)
print('{:^73}'.format('{}== Sequência de Fibonacci =={}'.format(cores['anil'], cores['clean'])))
print('{}=-={}'.format(cores['amarelo'], cores['clean'])*21)
n = int(input('>>Quantos termos você quer ler? '))
t1 = 0
t2 = 1
c = 3
print('{} > {} >'.format(t1, t2), end='')
while c <= n:
    t3 = t1 + t2
    print(' {}'.format(t3), end='')
    print(' >' if c < n else '', end='')
    t1 = t2
    t2 = t3
    c += 1
print('\n>>Fim da sequência! Obrigado!')
