from time import sleep


def title(msg):
    print('{}=-={}'.format('\033[1;36m', '\033[m') * 20)
    print(f'{msg:^60}')
    print('{}=-={}'.format('\033[1;36m', '\033[m') * 20)


def durma(segundos):
    sleep(segundos)


def contagem(i, f, p):
    print(f'>>Contagem de {i} até {f} contando de {p} em {p}:')
    durma(1.5)
    if p < 0:
        p *= -1
    if p == 0:
        print('Tu é gay man? Tais querendo bugar meu programa? Curto gay não!')
        print('>>Por causa da tua gayzice o passo agora vai ser 1!')
        durma(0.5)
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            durma(0.5)
            cont += p
        print(' >>FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            durma(0.5)
            cont -= p
        print(' >>FIM!')


title('>> CONTAGEM DE NÙMEROS <<')
contagem(1, 10, 1)
print('{}=-={}'.format('\033[1;36m', '\033[m')*20)
contagem(10, 1, 2)
print('{}=-={}'.format('\033[1;36m', '\033[m')*20)
print('>>Agora é sua vez de personalizar a contagem:')
init = int(input('>>Início: '))
fin = int(input('>>Final: '))
pas = int(input('>>Passo: '))
contagem(init, fin, pas)
