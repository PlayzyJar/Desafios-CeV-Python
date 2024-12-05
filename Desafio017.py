from math import hypot
co = float(input('     >>>Hipotesusa e Catetos<<< \n>>Informe o Comprimento do Cateto Oposto: '))
ca = float(input('>>Informe o comprimento do Cateto Adjascente: '))
hy = hypot(ca, co)
print('>>A Hipotenusa do triângulo CO:{}, CA:{} é {:.2f}'.format(co, ca, hy))
