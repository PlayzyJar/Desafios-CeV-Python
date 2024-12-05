from time import sleep
salario = float(input('>>Digite o valor do seu salário: R$'))
if salario <= 1250:
    print('>>Verificando...')
    sleep(1)
    print('>>Calculando aumento...')
    sleep(1)
    print('>>Você recebeu um aumento salarial de 15%!')
    print('>>Seu novo salário é de R${:.2f}'.format(salario+salario*0.15))
else:
    print('>>Verificando...')
    sleep(1)
    print('>>Calculando aumento...')
    sleep(1)
    print('>>Você recebeu um aumento salarial de 10%!')
    print('>>Seu novo salário é de R${:.2f}'.format(salario+salario*0.10))
print('>>Tenha um bom dia e trabalhe com segurança.')
