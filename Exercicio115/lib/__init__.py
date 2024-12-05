def linha(tam=15):
    print('\033[1;33m=-=\033[m' * tam)


def cabecalho(txt):
    linha()
    print(f'{txt:^45}')
    linha()
