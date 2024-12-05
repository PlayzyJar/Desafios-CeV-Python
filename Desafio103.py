def ficha(nome='>Desconhecido<', gols=0):
    if nome.strip() == '':
        nome = '>Desconhecido<'
    print('=-='*15)
    print(f'>>O jogador {nome} fez {gols} gols.')


n = str(input('>>Nome do jogador: '))
g = str(input('>>Quantos gols o jogador fez? '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
ficha(nome=n, gols=g)
