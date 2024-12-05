from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('>>Os númmeros sorteados foram:', n[0], n[1], n[2], n[3], n[4])
print(f'>>O maior valor é {max(n)}')
print(f'>>E o menor valor é {min(n)}')
