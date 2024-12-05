from time import sleep
print('\033[36m-=-'*20)
print('             >>Verificador de triângulos<<')
print('-=-'*20)
r1 = int(input('\033[m>>Informe o valor da primeira reta: '))
r2 = int(input('>>Informe o valor da segunda reta: '))
r3 = int(input('>>Informe o valor da terceira reta: '))
print('>>Processando...')
sleep(1)
if r1 + r2 >= r3 or r2 + r3 >= r1 or r3 + r1 >= r2:
    print('>>As retas {}, {} e {} podem formar um triângulo.'.format(r1, r2, r3))
else:
    print('>>As retas {}, {} e {} \033[1;31mNÃO\033[m podem formar um triângulo. '.format(r1, r2, r3))
