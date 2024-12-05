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


n = LeiaInt('>>Digite um número: ')
print(f'>>Você acabou de digitar o número {n}')
