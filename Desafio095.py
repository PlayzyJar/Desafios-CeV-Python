from time import sleep
cores = {0: '\033[1;33m', 1: '\033[m', 2: '\033[4;36m'}
res = 'S'
tot = partidas = v = 0
ficha = dict()
gols = list()
fichas = list()
print(f'{cores[0]}=-={cores[1]}'*20)
print(f'{"== CADASTRO DE JOGADORES ==":^60}')
print(f'{cores[0]}=-={cores[1]}'*20)
while True:
    while res in 'S':
        ficha['Nome'] = str(input('>>Nome do jogador: '))
        partidas = int(input(f'>>Quantas partidas {ficha["Nome"]} jogou? '))
        for c in range(0, partidas):
            gol = int(input(f'  >>Gols no {c+1}° jogo: '))
            gols.append(gol)
            tot += gol
        ficha['Gols'] = gols[:]
        gols.clear()
        ficha['Total'] = tot
        fichas.append(ficha.copy())
        ficha.clear()
        res = str(input('>>Continuar? [S/N]: ')).strip().upper()
        while res not in 'SN':
            res = str(input('>>Por favor digite S ou N: '))
    if v == 0:
        print(f'{cores[0]}=-={cores[1]}'*20)
        print(f'{"== TABELA DE JOGADORES ==":^60}')
        print(f'{cores[0]}=-={cores[1]}'*20)
        print(f'{"N° Jogador":^12}|{"Jogador":^20}|{"Gols":^18}|{"Total":^7}')
        for n, f in enumerate(fichas):
            print(f'     {n+1:0>2}     | {f["Nome"]:<18} |{str(f["Gols"]):^18}|{f["Total"]:^7}')
        print(f'{cores[0]}=-={cores[1]}' * 20)
        v += 1
    res2 = int(input('>>Mostrar informações de qual jogador? (999 to stop): '))
    if res2 == 999:
        print('>>Finalizando', end='')
        sleep(0.5)
        for a in range(0, 3):
            print('.', end='')
            sleep(0.5)
        break
    elif res2 > len(fichas):
        print('  >>Erro! Jogador não cadastrado, tente novamente.')
    else:
        print(f'  >>Levantamento do jogador {fichas[res2-1]["Nome"]}:')
        for b in range(0, len(fichas[res2-1]["Gols"])):
            print(f'    >>No {b+1}° jogo, fez {fichas[res2-1]["Gols"][b]} gol(s).')
        print(f'{cores[0]}=-={cores[1]}' * 20)
print('\n>>Programa encerrado. Volte sempre! :)')
print(f'\n{f"{cores[2]}Players Sign Up by PlayzyCovers.{cores[1]}":>70}')
