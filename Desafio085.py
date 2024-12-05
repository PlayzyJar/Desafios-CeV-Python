numeros = [[], []]
par = list()
impar = list()
for c in range(0, 7):
    temp = int(input(f'>>Digite o {c+1}° valor: '))
    if temp % 2 == 0:
        numeros[0].append(temp)
    elif temp % 2 != 0:
        numeros[1].append(temp)
    numeros.append(temp)
print('>>Os valores ÍMPARES digitados foram ', end='')
numeros[1].sort()
for pos, c in enumerate(numeros[1]):
    if pos < (len(numeros[1])-2):
        print(f'{c}', end=', ')
    elif pos == len(numeros[1])-2:
        print(f'{c}', end=' e ')
    else:
        print(c)
print('>>Os valores PARES digitados foram ', end='')
numeros[0].sort()
for pos, c in enumerate(numeros[0]):
    if pos < (len(numeros[0])-2):
        print(f'{c}', end=', ')
    elif pos == len(numeros[0])-2:
        print(f'{c}', end=' e ')
    else:
        print(c)
