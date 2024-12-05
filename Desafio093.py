tot = 0
gols = list()
ficha = dict()
ficha['Nome'] = str(input('>>Nome do Jogador: '))
partidas = int(input('>>Número de partidas: '))
for c in range(0, partidas):
    gol = (int(input(f'    >>Gols na {c+1}° partida: ')))
    gols.append(gol)
    tot += gol
ficha['Gols'] = gols
ficha['Total'] = tot
print('=-='*18)
print(ficha)
print('=-='*18)
for k, v in ficha.items():
    print(f'>>O campo {k} tem valor {v}')
print('=-='*18)
print(f'>>O jogador {ficha["Nome"]} jogou {partidas} partidas.')
for n in range(0, partidas):
    print(f'    >>Na {n+1}° partida, fez {gols[n]} gol(s).')
print(f'>>Total de {tot} gols.')

