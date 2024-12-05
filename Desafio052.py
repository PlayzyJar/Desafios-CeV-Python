tot = 0
n = int(input('>>Digite um número: '))
for c in range(1, n+1):
    if n % c == 0:
        print('\033[1;36m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[m>>O número {} foi divisível {} vezes.'.format(n, tot))
if tot == 2:
    print('>>{} é um número PRIMO!'.format(n))
elif tot != 2:
    print('>>{} NÃO é um número PRIMO!'.format(n))
