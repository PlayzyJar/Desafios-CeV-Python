from time import sleep
c = {0: '\033[m', 1: '\033[0;30;41m', 2: '\033[0;30;42m', 3: '\033[0;30;43m', 4: '\033[0;30;44m',
     5: '\033[0;30;45m', 6: '\033[0;30;46m', 7: '\033[7;30m'}


def ajuda(res):
    titulo(f'>>Acessando informações da função "{res}"...')
    print(c[7], end='')
    help(res)
    print(c[0], end='')
    sleep(2)


def titulo(msg):
    print('{}='.format(c[2])*(len(msg)+4))
    print(f'  {msg}')
    print('='.format(c[0])*(len(msg)+4))
    print(c[0], end='')
    sleep(1)

while True:
    titulo(' >> SISTEMA DE AJUDA INTERATIVA DO PYTHON <<')
    com = str(input('>>Nome da Função/Bibloteca: ')).lower()
    if com == 'fim':
        titulo('>>ENCERRANDO...')
        sleep(0.5)
        titulo('>> ATÉ LOGO! <<')
        break
    else:
        ajuda(com)
