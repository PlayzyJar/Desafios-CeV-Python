cambada = list()
pessoa = list()
res = 's'
maisleves = list()
maispesados = list()
mai = men = 0
while res in 'sim':
    pessoa.append(str(input('>>Nome da passoa: ')))
    pessoa.append(float(input('>>Peso da pessoa: ')))
    if len(cambada) == 0:
        mai = men = pessoa[1]
    elif pessoa[1] > mai:
        mai = pessoa[1]
    elif pessoa[1] < men:
        men = pessoa[1]
    cambada.append(pessoa[:])
    pessoa.clear()
    res = str(input('>>Continuar? [S/N]: ')).lower().strip()
    while res not in 'simnaonão':
        print('>>Resposta inválida!')
        res = str(input('>>Continuar? [S/N]: ')).lower().strip()
print(f'>>No total foram cadastradas {len(cambada)} pessoa(s).')
print(f'>>O maior peso cadastrado foi de {mai}kg. Peso de: ', end='')
for p in cambada:
    if p[1] == mai:
        print(f'={p[0]}=', end=' ')
print(f'\n>>O peso mais leve cadastrado foi de {men}kg. Peso de: ', end='')
for p in cambada:
    if p[1] == men:
        print(f'={p[0]}=', end=' ')
