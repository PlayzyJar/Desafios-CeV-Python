from time import sleep
cores = {'amarelo': '\033[1;33m',
         'azul': '\033[1;34m',
         'clean': '\033[m',
         'negrito': '\033[1m'}
print('{}=-={}'.format(cores['amarelo'], cores['clean'])*21)
print('{:^73}'.format('{}== MENU DE OPÇÕES =={}'.format(cores['azul'], cores['clean'])))
print('{}=-={}'.format(cores['amarelo'], cores['clean'])*21)
sleep(1)
n1 = int(input('{}>>Digite um valor: '.format(cores['negrito'])))
n2 = int(input('{}>>Digite outro valor: '.format(cores['negrito'])))
sleep(1)
print('''{}[1] SOMAR\n[2] MULTPLICAR\n[3] MAIOR
[4] NOVOS NÚMEROS \n[5] SAIR DO MENU{}'''.format(cores['azul'], cores['clean']))
sleep(1)
opcao = str(input('{}>>Escolha uma opção: '.format(cores['negrito'])))
while opcao != '5':
    if opcao == '1':
        soma = n1 + n2
        sleep(1)
        print('>>A soma entre {} e {} é {}'.format(n1, n2, soma))
        sleep(1)
        print('{}=-={}'.format(cores['amarelo'], cores['clean'])*21)
        print('''{}[1] SOMAR\n[2] MULTPLICAR\n[3] MAIOR
[4] NOVOS NÚMEROS\n[5] SAIR DO MENU{}'''.format(cores['azul'], cores['clean']))
        sleep(1)
        opcao = str(input('{}>>Escolha uma opção: '.format(cores['negrito'])))
    elif opcao == '2':
        produto = n1 * n2
        sleep(1)
        print('>>O produto da multiplicação entre {} e {} é {}'.format(n1, n2, produto))
        sleep(1)
        print('{}=-={}'.format(cores['amarelo'], cores['clean']) * 21)
        print('''{}[1] SOMAR\n[2] MULTPLICAR\n[3] MAIOR
[4] NOVOS NÚMEROS\n[5] SAIR DO MENU{}'''.format(cores['azul'], cores['clean']))
        sleep(1)
        opcao = str(input('{}>>Escolha uma opção: '.format(cores['negrito'])))
    elif opcao == '3':
        if n1 > n2:
            maior = n1
            sleep(1)
            print('>>Entre {} e {} o maior é {}'.format(n1, n2, maior))
            sleep(1)
        if n2 > n1:
            maior = n2
            sleep(1)
            print('>>Entre {} e {} o maior é {}'.format(n1, n2, maior))
            sleep(1)
        elif n1 == n2:
            sleep(1)
            print('>>Não há valor maior, os dois são iguais!')
            sleep(1)
        print('{}=-={}'.format(cores['amarelo'], cores['clean']) * 21)
        print('''{}[1] SOMAR\n[2] MULTPLICAR\n[3] MAIOR
[4] NOVOS NÚMEROS\n[5] SAIR DO MENU{}'''.format(cores['azul'], cores['clean']))
        sleep(1)
        opcao = str(input('{}>>Escolha uma opção: '.format(cores['negrito'])))
    elif opcao == '4':
        n1 = int(input('>>Digite um valor: '))
        n2 = int(input('>>Digite outro valor: '))
        print('{}=-={}'.format(cores['amarelo'], cores['clean']) * 21)
        print('''{}[1] SOMAR\n[2] MULTPLICAR\n[3] MAIOR
[4] NOVOS NÚMEROS\n[5] SAIR DO MENU{}'''.format(cores['azul'], cores['clean']))
        sleep(1)
        opcao = str(input('{}>>Escolha uma opção: '.format(cores['negrito'])))
print('>>Finalizando', end='')
for r in range(1, 4):
    print('.', end='')
    sleep(1)
print('\n>>Programa finalizado, volte sempre!')
