def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip().lower()
        if entrada.isalpha() or entrada == '':
            print(f'\033[1;31m>>Erro! "{entrada}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)


def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print('\033[1;31m>>Erro! Por favor, digite um número inteiro válido!\033[m')


def LeiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
            return n
        except ValueError:
            print('\033[1;31m>>Erro! Por favor, digite um número real válido!\033[m')
