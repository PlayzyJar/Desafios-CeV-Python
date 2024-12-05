from time import sleep
from random import randint
nums = list()


def generator():
    print('>>Sorteando números', end='')
    for c in range(0, 3):
        print('.', end='')
    print('\n>>', end='')
    cont = 0
    while cont < 5:
        n = randint(1, 10)
        if n not in nums:
            nums.append(n)
            cont += 1
    for v in nums:
        print(f'{v} ', end='')
        sleep(0.5)
    print()
    print('{}=-={}'.format('\033[1;36m', '\033[m')*20)


def somapar():
    soma = 0
    for n in nums:
        if n % 2 == 0:
           soma += n
    print(f'>>A soma dos pares dentre os valores listados acima é {soma}.')


generator()
somapar()
