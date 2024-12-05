cores = {'amarelo': '\033[1;33m',
         'anil': '\033[1;36m',
         'negrito': '\033[1m',
         'clean': '\033[m'}
cedulas = 0
valcedula = 50
print('{}=-='.format(cores['negrito'])*23)
print('{:^77}'.format('{}== CAIXA ELETRÔNICO PLAYZYBANK =={}'.format(cores['anil'], cores['clean'])))
print('{}=-='.format(cores['negrito'])*23)
total = sacar = int(input('>>Digite o valor que deseja sacar: R$'))
while True:
    if total >= valcedula:
        total -= valcedula
        cedulas += 1
    else:
        if cedulas > 0:
            print(f'>>Total de {cedulas} cédulas de R${valcedula:.2f}')
        if valcedula == 50:
            valcedula = 20
        elif valcedula == 20:
            valcedula = 10
        elif valcedula == 10:
            valcedula = 1
        cedulas = 0
        if total == 0:
            break
print('>>Volte sempre ao PlayzyBank! Tenha um bom dia!')
