from time import sleep
import datetime
gen = str(input('>>Qual o seu gênero?\n[1] FEMININO\n[2] MASCULINO\n>>Sua opção: ')).strip().lower()
print('Processando', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.')
sleep(0.5)
if gen == '1':
    print('>>Você não precisa se apresentar no exército.')
elif gen == '2':
    anonasc = int(input('>>Em que ano você nasceu? '))
    anoatual = datetime.date.today().year
    idade = anoatual - anonasc
    print('>>Quem nasceu em {} tem {} anos em {}'.format(anonasc, idade, anoatual))
    if idade == 18:
        print('>>Você deve se alistar IMEDIATAMENTE!')
    elif idade < 18:
        anosres = 18 - idade
        anoalis = anosres + anoatual
        print('>>Ainda faltam {} ano(s) para o seu alistamento'.format(anosres))
        print('>>Seu alistamento será em {}'.format(anoalis))
    elif idade > 18:
        anospas = idade - 18
        anoalis = anonasc + 18
        print('>>Você deveria ter se apresentado há {} ano(s)'.format(anospas))
        print('>>Seu alistamento foi em {} '.format(anoalis))
