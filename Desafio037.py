from time import sleep
print('          >>Coversor de Bases Numéricas<<')
n = int(input('>>Digite um número inteiro: '))
opcao = str(input('>>Converter para: \n[1] BINÁRIO\n[2] OCTAL\n[3] HEXADECIMAL\n>>Sua opção: '))
if opcao == '1':
    print('>>Covertendo', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('{} covertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif opcao == '2':
    print('>>Covertendo', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('{} covertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif opcao == '3':
    print('>>Covertendo', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('{} covertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('>>Opção inválida, tente novamente!')