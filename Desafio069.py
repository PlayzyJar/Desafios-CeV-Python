from time import sleep
mulheres = tot = homens = maioridade = 0
res = 'c'
while res not in 'Nn':
    gen = res = 'c'
    print('=-='*23)
    print('{:^69}'.format(' == CADASTRE UMA PESSOA =='))
    print('=-='*23)
    idade = int(input('>>Idade: '))
    while gen not in 'FM':
        gen = str(input('>>Gênero [F/M]: ')).strip().upper()[0]
    if idade >= 18:
        maioridade += 1
    if gen in 'Mm':
        homens += 1
    if idade < 20 and gen in 'Ff':
        mulheres += 1
    print('>>Validando dados', end='')
    sleep(1)
    for c in range(0, 3):
        print('.', end='')
        sleep(0.5)
    print('\n>>Dados validados com sucesso.')
    tot += 1
    sleep(0.5)
    res = str(input('>>Cadastrar mais uma pessoa [Sim/Não]? ')).strip().lower()[0]
    while res not in 'SsNn':
        res = str(input('>>Cadastrar mais uma pessoa [Sim/Não]? ')).strip().lower()[0]
print('=-='*23)
print(f'>>Foram cadastrados os dados de {tot} pessoas.')
print(f'>>Dentre essas pessoas:\n>>Tivemos {maioridade} pessoas maiores de idade.')
print(f'>>Ao todo {homens} homem(s) foram cadastrados.\n>>E tivemos {mulheres} mulher(es) com mais de 20 anos.')
