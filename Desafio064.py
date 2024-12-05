cont = soma = 0
cores = {'negrito': '\033[1m'}
print('{}=-='.format(cores['negrito'])*23, '\n', '{:^71}'.format('== LEITOR DE NÚMEROS =='))
print('=-='*23)
n = int(input('>>Informe um valor:\n[999] Para parar\n>>Valor: '))
while n != 999:
    soma += n
    cont += 1
    print('=-='*23)
    n = int(input('>>Informe um valor:\n[999] Para parar\n>>Valor: '))
print('>>No total foram lidos {} valores e a soma entre eles é {}'.format(cont, soma))
