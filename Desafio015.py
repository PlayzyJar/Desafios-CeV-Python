d = int(input('      >>>Aluguel de Carros<<< \n>>Quantos dias você passou com o carro? '))
km = int(input('>>Quantos quilômetros você rodou? '))
vt = (d * 60) + (km * 0.15)
print('>>O valor a ser pago é R${:.2f} \n \n                                >>Obrigado!'.format(vt))
