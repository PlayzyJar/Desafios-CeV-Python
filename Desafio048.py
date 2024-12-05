c = 0
s = 0
print('=-='*21, '\n', '{:^60}'.format('>>SOMA DE IMPARES MÚLTIPLOS DE 3<<'))
print('=-='*21)
for m in range(1, 501):
    if m % 2 != 0 and m % 3 == 0:
        c += 1
        s += m
print('\n>>A soma de todos os {} valores solicitados é igual a {}.'.format(c, s))
