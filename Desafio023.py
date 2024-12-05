n1 = int(input('      >>>Separador de Dígitos<<< \n>>Digite um número de 1 à 9999: '))
print('>>Analizando... \n>>Unidade: {} \n>>Dezena: {}'.format(n1 // 1 % 10, n1 // 10 % 10))
print('>>Centena: {} \n>>Milhar: {}'.format(n1 // 100 % 10, n1 // 1000 % 10))
