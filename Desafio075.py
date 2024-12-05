par = 0
npar = ''
n = (int(input('>>Digite o 1° valor: ')),
     int(input('>>Digite o 2° valor: ')),
     int(input('>>Digite o 3° valor: ')),
     int(input('>>Digite o 4°  valor: ')))
if n.count(9) == 0:
    print('>>O número 9 não foi digitado nenhuma vez.')
elif n.count(9) == 1:
    print(f'>>O número 9 foi digitado {n.count(9)} vez.')
else:
    print(f'>>O número 9 foi digitado {n.count(9)} vezes.')
if 3 not in n:
    print('>>O número 3 não foi digitado nehuma vez.')
else:
    print(f'>>O primeiro número 3 foi digitado na {n.index(3)+1}° vez.')
for c in range(0, 4):
    if n[c] % 2 == 0:
        par += 1
if par > 0:
    print('>>Os números pares digitados foram: ', end='')
    for cont in n:
        if cont % 2 == 0:
            print(cont, end=' ')
else:
    print('>>Não foi digitado nenhum valor par.')
