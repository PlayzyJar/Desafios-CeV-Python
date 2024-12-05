print('=-='*23)
print('{:^69}'.format('== ATACADÃO TABAJARA =='))
print('=-='*23)
res = 's'
cont = pmaisbarato = pmaisdemil = total = nmaisbarato = 0

while res in 'Ss':
    produto = str(input('>>Nome do produto: '))
    preco = float(input('>>Preço: R$'))
    res = str(input('>>Continuar [Sim/Não]? ')).strip().upper()[0]
    if preco >= 1000:
        pmaisdemil += 1
    cont += 1
    total += preco
    if cont == 1 or preco < pmaisbarato:
        nmaisbarato = produto
        pmaisbarato = preco
print('{:-^69}'.format(' FIM DO PROGRAMA '))
print(f'>>O total da compra foi de R${total:.2f}')
print(f'>>{pmaisdemil} produto(s) custaram mais de R$1000.00')
print(f'>>E o produto mas barato foi {nmaisbarato} que custou R${pmaisbarato:.2f}')
