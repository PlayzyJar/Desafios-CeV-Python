nmulheres = peoples = idades = 0
peoplesUP = list()
dados = dict()
cambada = list()
mulheres = list()
res = 'S'
while res in 'S':
    dados['Nome'] = str(input('>>Nome: '))
    dados['Sexo'] = str(input('>>Sexo [M/F]: ')).strip().upper()
    while dados['Sexo'] not in 'FM':
        dados['Sexo'] = str(input('>>Valor inválido! Por favor digite M ou F: ')).strip().upper()
    if dados['Sexo'] == 'F':
        mulheres.append(dados['Nome'])
        nmulheres += 1
    dados['Idade'] = int(input('>>Idade: '))
    idades += dados['Idade']
    peoples += 1
    res = str(input('>>Continuar? [S/N]: ')).strip().upper()
    while res not in 'SN':
        res = str(input('>>Valor inválido! Por favor, digite S ou N: ')).strip().upper()
    cambada.append(dados.copy())
    dados.clear()
media = idades / peoples
for num, c in enumerate(cambada):
    if cambada[num]['Idade'] > media:
        peoplesUP.append(c.copy())
print('{}=-={}'.format('\033[1;33m', '\033[m')*22)
print(f'A) >>Foram cadastradas um total de {peoples} pessoas.')
print(f'B) >>A média de idade das pessoas cadastradas foi de {media:.1f} anos.')
if nmulheres > 0:
    print(f'C) >>Lista das mulheres cadastradas: ')
    for c, n in enumerate(mulheres):
        if c < len(mulheres)-1:
            print(n, end=' e ')
        else:
            print(n)
else:
    print('C) >>Não foi cadastrada nenhuma mulher.')
if len(peoplesUP) > 0:
    print('D) >>Lista de pessoas com idade acima da média:')
    for p, val in enumerate(peoplesUP):
        print(f'    >>Nome: {peoplesUP[p]["Nome"]}; Sexo: {val["Sexo"]}; ', end='')
        print(f'Idade: {val["Idade"]}')
else:
    print('D) >>Não há ninguém acima da média de idade.')
