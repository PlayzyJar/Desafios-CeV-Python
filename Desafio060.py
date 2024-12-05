num = int(input('>>Digite um número para calcular seu fatorial: '))
f = 1
print('>>Calculando fatorial de {}!'.format(num), end=' = ')
c = num
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
