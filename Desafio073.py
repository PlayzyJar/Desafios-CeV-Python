from time import sleep
sop = 20
tabela = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
          'Flamengo', 'Vasco da Gama', 'Chapecoense', 'Atlético', 'Botafogo',
          'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
          'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('=-='*30)
print('{:^90}'.format('== TABELA BRASILEIRÃO 2018 =='))
print('=-='*30)
res = ' '
while res not in '6':
    print('>>MENU DE OPÇÕES DA TABELA: \n\n[1] MOSTRAR TABELA COMPLETA\n[2] OS CINCO PRIMEIROS COLOCADOS')
    print('[3] OS QUATRO ÚLTIMOS COLOCADOS\n[4] MOSTRAR POSIÇÃO DO CHAPECOENSE\n[5] TIMES EM ORDEM ALFABÉTICA')
    res = str(input('[6] SAIR DO PROGRAMA\n\n>>Escolha uma das opcões acima: '))
    print('=-='*30)
    while res not in '123456':
        res = str(input('>>Por favor, insira uma opção válida: '))
        print('=-='*30)
    if res == '1':
        print('>>TABELA TOP#20 BRASILEIRÃO:\n')
        for pos, time in enumerate(tabela):
            print(f'{pos+1}°', time)
            sleep(0.3)
    elif res == '2':
        print('>>TABELAS TOP#5 BRASILEIRÃO:\n')
        for pos, time in enumerate(tabela[0:5]):
            print(f'{pos+1}°', time)
            sleep(0.3)
    elif res == '3':
        print('>>TABELA QUATRO ÙTIMOS COLOCADOS:\n')
        for time in tabela[20:15:-1]:
            print(f'{sop}°', time)
            sop -= 1
            sleep(0.3)
    elif res == '4':
        print(f'>>O Chapecoense está em {tabela.index("Chapecoense")+1}° lugar.')
    elif res == '5':
        print('>>TABELA EM ORDEM ALFABÉTICA:\n')
        tabordem = sorted(tabela)
        for time in tabordem:
            print('>>', time)
            sleep(0.3)
    print('=-='*30)
print('>>Encerrando programa', end='')
sleep(1)
for c in range(0, 3):
    print('.', end='')
    sleep(1)
print('\n>>Programa encerrado. Até a próxima!')
