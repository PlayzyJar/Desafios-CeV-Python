alt = float(input('            >>Teste de IMC<<\n>>Qual a sua altura em metros? '))
peso = float(input('>>Qual o seu peso em Kg? '))
IMC = peso / (alt**2)
print('>>O seu IMC é de {:.1f}'.format(IMC))
if IMC < 18.5:
    print('>>Você está ABAIXO do peso ideal.')
elif 18.5 <= IMC < 25:
    print('Você está no peso IDEAL!')
elif 25 <= IMC < 30:
    print('>>Você está ACIMA do peso ideal.')
elif 30 <= IMC < 40:
    print('>>Você está OBESO!')
elif IMC >= 40:
    print('>>Você está em OBESIDADE MÓRBIDA! Cuidado!')
