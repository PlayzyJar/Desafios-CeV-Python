valor = total = float(input())

cedulaatual = [100, 50, 20, 10, 5, 2]
qtdcedulas = [0, 0, 0, 0, 0, 0]
moedaatual = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
qtdmoedas = [0, 0, 0, 0, 0, 0]


for cont, cedula in enumerate(cedulaatual):
    qtdcedulas[cont] = int(total / cedula)
    total -= qtdcedulas[cont] * cedula


print('NOTAS:')
for cont, nota in enumerate(qtdcedulas):
    print(f'{nota} nota(s) de R$ {cedulaatual[cont]:.2f}')

for cont, moeda in enumerate(moedaatual):
    qtdmoedas[cont] = int(round(total, 2) / moeda)
    total -= (qtdmoedas[cont] * moeda)

print('MOEDAS:')
for cont, moeda in enumerate(qtdmoedas):
    print(f'{moeda} moeda(s) de R$ {moedaatual[cont]:.2f}')
    cont += 1
