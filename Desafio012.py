p = float(input('      >>>Promoção 5%off<<< \n>>Informe o preço do produto: R$'))
pcd = p - (p * 0.05)
print('>>Este produto de R${:.2f} na promoção 5%off vai ficar por R${:.2f}. \n >>Obrigado! \n                           >>Organizações Tabajara<<'.format(p, pcd))
