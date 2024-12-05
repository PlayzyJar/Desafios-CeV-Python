from time import sleep
from datetime import date
print('-=-'*20, '\n               >>Classificação de Atletas<<\n', '-=-'*20)
nasc = int(input('>>Ano de nascimento: '))
print('>>Classificando atleta', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.')
sleep(0.5)
idade = date.today().year - nasc
print('>>O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('>>Atleta de categoria MIRIM.')
elif 9 < idade <= 14:
    print('>>Atleta de categoria INFANTIL.')
elif 14 < idade <= 19:
    print('>>Atleta de categoria JUNIOR.')
elif 19 < idade <= 25:
    print('>>Atleta de categoria SÊNIOR.')
elif idade > 25:
    print('>>Atleta de categoria MASTER.')
