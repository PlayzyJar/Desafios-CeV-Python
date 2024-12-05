def area(large, comp):
    aterr = large * comp
    print(f'>>A área de um terreno de {large}x{comp} metros é igual a {aterr:.1f}m².')


def title(msg):
    print('{}=-={}'.format('\033[1;36m', '\033[m') * 20)
    print(msg)
    print('{}=-={}'.format('\033[1;36m', '\033[m') * 20)


title(f'{">> CÁLCULO DE ÁREA DE TERRENO <<":^60}')
large = float(input('>>Qual a largura do terreno em metros? '))
comp = float(input('>>Qual o comprimento do terreno em metros? '))
area(large, comp)
