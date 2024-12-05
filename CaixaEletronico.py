valor = total = int(input())
print(valor)
cedulaatual = [100, 50, 20, 10, 5, 2, 1]
qtdcedulas = [0, 0, 0, 0, 0, 0, 0]
cont = 0
while True:
    if total > 0:
        qtdcedulas[cont] = total // cedulaatual[cont]
        total -= qtdcedulas[cont] * cedulaatual[cont]
        cont += 1

    else:
        cont = 0
        break

for c in qtdcedulas:
    print(f'{c} notas de R$ {cedulaatual[cont]:.2f}'.replace('.', ','))
    cont += 1
