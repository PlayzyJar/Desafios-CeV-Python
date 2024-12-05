lista = list()
pos = 0
res = 's'
print('{}=-={}'.format('\033[1;33m', '\033[m')*23)
print('{:^76}'.format('{}== EXTRATOR DE VALORES =={}'.format('\033[1;36m', '\033[m')))
print('{}=-={}'.format('\033[1;33m', '\033[m')*23)
while res in 'sim':
    lista.append(int(input('{}>>Digite um valor: '.format('\033[1m'))))
    res = str(input('>>Continuar [S/N]? ')).strip().lower()
    while res not in 'simnaonão':
        res = str(input('>>Resposta inválida, tente novamente: '))
print('=-='*23)
print(f'>>No total foram digitados {len(lista)} valores.')
lista.sort(reverse=True)
print('>>Os números digitados em ordem decrescente são: ', end='')
for p, num in enumerate(lista):
    if p < len(lista)-1:
        print(num, end=', ')
    else:
        print(num)
if 5 in lista:
    print('>>E o número 5 está dentro dos valores digitados.')
else:
    print('>>O número 5 não está presente dentre os valores digitados.')
