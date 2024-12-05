from random import randint
from time import sleep
from operator import itemgetter
players = dict()
ranking = list()
print('=-='*18)
print(f'{"Jogo de Dados":^54}')
print('=-='*18)
print('            >>> Valores Sorteados <<<')
for d in range(1, 5):
    players[f'Player{d}'] = randint(1, 6)
    print(f'>>Player {d} tirou {players[f"Player{d}"]}')
    sleep(0.5)
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
print(f'{" Placar ":=^54}')
for p, v in enumerate(ranking):
    print(f'{p+1:>3}° lugar: {v[0]} com {v[1]}')
