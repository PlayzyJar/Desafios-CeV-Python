cont = 0
menor = maior = n = soma = 0
res = 'S'
while res in 'Ss':
    n = int(input('>>Digite  um valor: '))
    res = str(input('Continuar? [S/N]: ')).upper().strip()[0]
    print('=-='*23)
    soma += n
    if cont == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cont += 1
print('>>A média entre os {} valores digitados é {:.1f}'.format(cont, soma/cont))
print('>>O maior valor digitado foi {} e o menor foi {}.'.format(maior, menor))
print(res)
