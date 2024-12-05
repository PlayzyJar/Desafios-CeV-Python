from time import sleep
alunos = []
nota = []
res = 's'
cont = v = 0
while res in 'sim':
    nota.append(str(input('>>Aluno: ')))
    nota.append(float(input('>>1° nota: ')))
    nota.append(float(input('>>2° nota: ')))
    alunos.append(nota[:])
    nota.clear()
    res = str(input('>>Continuar [Sim/Não]: ')).strip().lower()
    while res not in 'simnaonão':
        print('>>Resposta inválida! ')
        res = str(input('>>Continuar [Sim/Não]: ')).strip().lower()
print('{}=-={}'.format('\033[1;33m', '\033[m')*17)
print(' N° Aluno |       Aluno       | Média')
while cont < len(alunos):
    print(f'    {cont+1:0>2}°   | {alunos[cont][0]:<17} | {(alunos[cont][1]+alunos[cont][2])/2:>4.1f}')
    cont += 1
print('{}=-={}'.format('\033[1;33m', '\033[m')*17)
res2 = int(input('>>Mostrar notas de qual aluno? (999 interrompe): '))
while True:
    if res2 in range(1, cont+1):
        print('{}=-={}'.format('\033[1;33m', '\033[m')*17)
        print(f'>>As notas de {alunos[res2-1][0]} são {alunos[res2-1][1]} e {alunos[res2-1][2]}')
        print('{}=-={}'.format('\033[1;33m', '\033[m')*17)
        res2 = int(input('>>Mostrar notas de qual aluno? (999 interrompe): '))
        if res2 == 999:
            print('>>Finalizando', end='')
            for r in range(0, 3):
                print('.', end='')
                sleep(1)
            break
    elif res2 not in range(1, cont+1):
        print('>>Aluno não cadastrado. Tente novamente')
        res2 = int(input('>>Mostrar notas de qual aluno? (999 interrompe): '))
        if res2 == 999:
            print('>>Finalizando', end='')
            for r in range(0, 3):
                print('.', end='')
                sleep(1)
            break
    elif res2 == 999:
        print('>>Finalizando', end='')
        for r in range(0, 3):
            print('.', end='')
            sleep(1)
        break
print('\n>>Programa encerrado, volte sempre! :)')
