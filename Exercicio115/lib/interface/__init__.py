c = {0: '\033[m', 1: '\033[1;33m', 2: '\033[1;34m', 3: '\033[1m'}


def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print('\033[1;31m>>Erro! Por favor, digite o número de uma das \nopções listadas acima!\033[m')


def linha(tam=15):
    print('\033[1;33m=-=\033[m' * tam)


def cabecalho(txt):
    linha()
    print(f'\033[1;34m{txt:^45}\033[m')
    linha()


def menu(lista):
    cabecalho('>> MENU PRINCIPAL <<')
    cont = 1
    for item in lista:
        print(f'>>{c[1]}[{c[0]}{c[3]}{cont}{c[0]}{c[1]}]{c[0]} {c[2]}{item}{c[0]}')
        cont += 1
    linha()
    res = LeiaInt('>>\033[1;34mSua opção: \033[m')
    return res
