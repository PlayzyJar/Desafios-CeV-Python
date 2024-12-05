maisp = 0
menosp = 0
peso = 0
for p in range(1, 6):
    peso = float(input('>>Digite o peso da {}° pessoa: '.format(p)))
    if p == 1:
        maisp = peso
        menosp = peso
    if peso > maisp:
        maisp = peso
    elif peso < menosp:
        menosp = peso
print('>>O maior peso digitado foi de {}Kg'.format(maisp))
print('>>E o menor peso foi de {}Kg'.format(menosp))
