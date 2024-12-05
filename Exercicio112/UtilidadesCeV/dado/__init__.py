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
    valor = 0
    isint = False
    while not isint:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            isint = True
        else:
            print('\033[1;31m>>Erro! Por favor, digite um número inteiro válido!\033[m')
    return valor
