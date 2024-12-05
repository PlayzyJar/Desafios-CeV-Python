posmaior = list()
posmenor = list()
valores = list()
for c in range(0, 5):
    valores.append(int(input(f'>>Digite o valor da posição {c+1}: ')))
print('=-='*23)
for pos, v in enumerate(valores):
    if v == max(valores):
        posmaior.append(pos)
    if v == min(valores):
        posmenor.append(pos)
print(f'>>O maior valor digitado foi {max(valores)} nas posições: ', end='')
for m in posmaior:
    print(f'{m+1}', end=' ')
print(f'\n>>O menor valor digitado foi {min(valores)} nas posições: ', end='')
for m in posmenor:
    print(f'{m+1}', end=' ')
