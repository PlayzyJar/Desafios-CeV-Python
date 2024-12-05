from time import sleep
from random import randint
attempts = res3 = 1
while res3 == 1:
    machine = randint(0, 10)
    print('=-='*24, '\n', '{:^71}'.format('>>JOGO DA ADIVINHAÇÃO v2.0<<'))
    print('=-='*24)
    print('\n>>The  Machine: \n>>Eu vou pensar em um número de 0 à 10, você conssegue adivinhar qual é? ')
    res1 = str(input('[1] Yes \n[2] No\n>>Sua escolha: '))
    print('=-='*24)
    if res1 == '1':
        print('>>Pensando', end='')
        sleep(0.5)
        for r in range(1, 4):
            print('.', end='')
            sleep(0.5)
        print('')
        print('=-='*24)
        res2 = int(input('>>Qual número eu pensei? '))
        while res2 != machine:
            if res2 < machine:
                res2 = int(input('>>Errou! era maior, tente denovo: '))
            elif res2 > machine:
                res2 = int(input('>>Errou! Era menor, tente novamente: '))
            attempts += 1
        print('=-='*24)
        if 2 > attempts > 1:
            print('>>The Machine: \n>>Você acertou! Mas não foi de primeira.')
            print('>>Você ainda é um humano fraco e inferior a mim!')
            res3 = int(input('>>Play Again? \n[1] Yes\n[2] No\n>>Your Choice:'))
        elif 11 > attempts > 2:
            print('>>The Machine: \n>>Você acertou! Porém em {} tentativas!'.format(attempts))
            print('>>Isso só prova que máquinas são muito superiores a vocês!')
            res3 = int(input('>>Play Again? \n[1] Yes \n[2] No\n>>Your Choice:'))
        elif attempts == 11:
            print('>>The Machine: \n>>Até que enfim! Sabia que humanos eram lerdos mas isso é demais!')
            res3 = int(input('>>Play Again? \n[1] Yes \n[2] No\n>>Your Choice:'))
        elif attempts == 1:
            print('>>The Machine: \n>>Parabéns! Você acertou, e de primeira!')
            print('''>>Sempre falei que máquinas são superiores, mas você é o primeiro que se 
equiparou a mim. Tiro meu chapéu para você bravo guerreiro!''')
            res3 = int(input('>>Play Again? \n[1] Yes \n[2] No\n>>Your Choice:'))

    else:
        print('=-='*24, '\n>>The Machine: \n>>Arregou! Você é fraco, humano inferior!')
        res3 = int(input('>>Play Again? \n[1] Yes \n[2] No\n>>Your Choice:'))
    attempts = 0
