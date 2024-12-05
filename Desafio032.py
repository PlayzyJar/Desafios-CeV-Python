from datetime import date
from time import sleep
ano = int(input('>>Qual ano você quer analisar? Para analisar o ano atual tecle 0: '))

if ano == 0:
    ano = date.today().year

if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print('>>Analizando...')
    sleep(2)
    print('>>{} é um ano BISSEXTO.'.format(ano))

else:
    print('>>Analizando...')
    sleep(2)
    print('>>{} NÃO é um ano BISSEXTO.'.format(ano))
