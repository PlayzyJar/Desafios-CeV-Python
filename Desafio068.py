import pygame
from time import sleep
from random import randint
cores = {'amarelo': '\033[1;33m',
         'anil': '\033[1;36m',
         'negrito': '\033[1m',
         'clean': '\033[m'}
wins = 0
playagain = '1'
while playagain == '1':
    pygame.mixer.init()
    pygame.mixer.music.load('Desafio045.mp3')
    pygame.mixer.music.play()
    while True:
        machine = randint(0, 100)
        print('{}=-={}'.format(cores['amarelo'], cores['clean']) * 23)
        print('{:^78}'.format('{}== PAR or ÍMPAR =={}'.format(cores['anil'], cores['clean'])))
        print('{}=-={}'.format(cores['amarelo'], cores['clean']) * 23)
        res1 = str(input('\n>>Escolha uma arma matemática: \n[P] Par\n[I] Ímpar\n>>Sua arma: ')).upper().strip()[0]
        res2 = int(input('>>Agora, escolha um número qualquer: '))
        if res1 == 'P' and (machine + res2) % 2 == 0:
            print('{}=-={}'.format(cores['amarelo'], cores['clean'])*23)
            print(f'>>Machine escolheu a arma Ímpar e o número {machine}')
            print(f'>>Player One escolheu a arma Par e o número {res2}')
            print(f'>>Total = {machine + res2} = Par!')
            print('>>Player One Wins!!!')
            print('>>Let`s play again', end='')
            for c in range(0, 3):
                print('.', end='')
                sleep(1)
            wins += 1
            print('')
            print('{}=-={}'.format(cores['amarelo'], cores['clean'])*23)
        elif res1 == 'P' and (machine + res2) % 2 != 0:
            print('{}=-={}'.format(cores['amarelo'], cores['clean']) * 23)
            print(f'>>Machine escolheu a arma Ímpar e o número {machine}')
            print(f'>>Player One escolheu a arma Par e o número {res2}')
            print(f'>>Total = {machine + res2} = Ímpar!')
            if wins == 1:
                print(f'>>Machine Wins! \n>>Player One teve 1 acerto consecutivo!')
            elif wins > 1:
                print(f'>>Machine Wins!\n >>Player One alcancou um total de {wins} vitórias consecutivas!')
            elif wins < 1:
                print('>>Machine Wins! Fawnless Victory')
            break
        elif res1 == 'I' and (machine + res2) % 2 != 0:
            print('{}=-={}'.format(cores['amarelo'], cores['clean']) * 23)
            print(f'>>Machine escolheu a arma Par e o número {machine}')
            print(f'>>Player One escolheu a arma Ímpar e o número {res2}')
            print(f'>>Total = {machine + res2} = Ímpar!')
            print('>>Player One Wins!!!')
            print('>>Let`s play again', end='')
            for c in range(0, 3):
                print('.', end='')
                sleep(1)
            wins += 1
            print('')
            print('{}=-={}'.format(cores['amarelo'], cores['clean']) * 23)
        elif res1 == 'I' and (machine + res2) % 2 == 0:
            print('{}=-={}'.format(cores['amarelo'], cores['clean']) * 23)
            print(f'>>Machine escolheu a arma Par e o número {machine}')
            print(f'>>Player One escolheu a arma Ímpar e o número {res2}')
            print(f'>>Total = {machine + res2} = Par!')
            if wins == 1:
                print(f'>>Machine Wins! \n>>Player One teve 1 acerto consecutivo!')
            elif wins > 1:
                print(f'>>Machine Wins!\n >>Player One alcancou um total de {wins} vitórias consecutivas!')
            elif wins < 1:
                print('>>Machine Wins! Fawnless Victory')
            break
    playagain = str(input('>>Play Again?\n[1] Yes\n[2] No\n>>Your choice: '))
print('\n \n  >>Créditos: Created by {}PlayzyCovers{}'.format(cores['anil'], cores['clean']))
