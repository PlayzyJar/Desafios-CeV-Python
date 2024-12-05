from datetime import date
maiorid = 0
menorid = 0
for c in range(1, 8):
    nasc = int(input('>>Digite o ano de nascimento da {}° pessoa: '.format(c)))
    if date.today().year - nasc >= 21:
        maiorid += 1
    elif date.today().year - nasc < 21:
        menorid += 1
print('>>Nesse grupo de pessoas há {} maior(es) de idade.'.format(maiorid))
print('>>E há também {} menor(es) de idade'.format(menorid))
