from time import sleep
cores = {'verde': '\033[4;32m',
         'amarelo': '\033[4;33m',
         'vermelho': '\033[4;31m',
         'clean': '\033[m'}
n1 = float(input('>>Primeira nota: '))
n2 = float(input('>>Segunda nota: '))
media = (n1 + n2) / 2
print('>>Calculando média', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.')
sleep(0.5)
print('>>Com as notas {} e {}, a média é {:.1f}'.format(n1, n2, media))
sleep(0.5)
if media >= 7:
    print('>>O aluno foi {}APROVADO!{}'.format(cores['verde'], cores['clean']))
elif 5 <= media <= 6.9:
    print('>>O aluno está em {}RECUPERAÇÃO{}'.format(cores['amarelo'], cores['clean']))
elif media < 5:
    print('>>O aluno foi {}REPROVADO!{}'.format(cores['vermelho'], cores['clean']))
