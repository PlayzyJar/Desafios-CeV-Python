numbers = list()
res = 's'
while res in 'sim':
    num = int(input('>>Digite um valor: '))
    if num not in numbers:
        numbers.append(num)
        print('>>Valor adicionado com sucesso! ')
    else:
        print('>>Esse valor já foi adicionado!')
        print('>>Não irei adicionálo denovo...')
    res = str(input('>>Continuar [S/N]? ')).lower().strip()
    while res not in 'simnãonao':
        res = str(input('>>Resposta inválida, por favor, digite novamente: ')).strip().lower()
print('=-='*23)
print('>>Os valores adicionados foram: ', end='')
numbers.sort()
for pos, n in enumerate(numbers):
    if pos < (len(numbers)-1):
        print(n, end=', ')
    else:
        print(n)
