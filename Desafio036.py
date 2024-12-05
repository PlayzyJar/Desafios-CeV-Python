from time import sleep
cores = {'verde': '\033[4;32m',
         'vermelho': '\033[4;31m',
         'clean': '\033[m'}
print('                    >>>PlayzyBank<<<\n')
sleep(0.5)
preco = float(input('>>Qual o valor da casa que o senhor(a) deseja comprar? R$'))
salario = float(input('>>Qual o valor do seu salário bruto mensal? R$'))
years = int(input('>>Em quantos anos o senhor deseja pagar a casa? '))
meses = years * 12
persal = salario * 0.30
parcelas = preco / meses
print('>>Analizando', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(0.5)
if parcelas <= persal:
    print('>>Para pagar uma casa de R${:.2f} em {} anos, o valor da parcela será de R${:.2f} '.format(preco, years, parcelas))
    sleep(5)
    print('>>O empréstimo pode ser {}CONCEDIDO{}!'.format(cores['verde'], cores['clean']))
elif parcelas > persal:
    print('>>Para pagar uma casa de R${:.2f} em {} anos, o valor da parcela será de R${:.2f} '.format(preco, years, parcelas))
    sleep(5)
    print('>>Empréstimo {}NEGADO!{}'.format(cores['vermelho'], cores['clean']))
