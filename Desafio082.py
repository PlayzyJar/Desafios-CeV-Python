lista = []
pares = []
impares = []
res = 's'
while res not in 'naonão':
    num = (int(input('>>Digite um número: ')))
    if num % 2 == 0:
        pares.append(num)
    elif num % 2 != 0:
        impares.append(num)
    lista.append(num)
    res = str(input('>>Continuar? [S/N]: '))
    while res not in 'simnaonão':
        res = str(input('>>Resposta inválida, tente novamente: '))
print('=-='*25)
print('>>A lista completa é: ', end='')
for pos, n in enumerate(lista):
    if pos < len(lista)-1:
        print(n, end=', ')
    else:
        print(f'{n}.')
print('>>A lista dos números PARES é: ', end='')
for pos, n in enumerate(pares):
    if pos < len(pares)-1:
        print(n, end=', ')
    else:
        print(f'{n}.')
print('>>A lista dos números ÍMPARES é: ', end='')
for pos, n in enumerate(impares):
    if pos < len(impares)-1:
        print(n, end=', ')
    else:
        print(f'{n}.')
