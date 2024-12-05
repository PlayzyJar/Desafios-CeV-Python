sa = float(input('           >>Reajuste Salarial<< \n>>Qual o salário atual do funcionário? R$'))
nv = sa + (sa * 0.15)
print('>>O salário bruto do funcionário que era de R${:.2f}, agora com o aumento de 15% ficou R${:.2f}.'.format(sa, nv))
