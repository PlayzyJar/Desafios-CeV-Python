alt = float(input('       >>>Ajudante para Pintores<<< \n>>Qual a altura da sua parede? '))
com = float(input('>>Qual a largura da parede? '))
area = alt * com
l = area / 2
print('>>As medidas da sua parede são {}x{} e a área é {:.4f}m²\n>>Considerando que com 1l de tinta dá para pintar 2m² você irá precisar de {:.4f}l de tinta'.format(alt, com, area, l))
