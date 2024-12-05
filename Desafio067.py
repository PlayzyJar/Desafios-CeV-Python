print('=-='*23, '\n', '{:^69}'.format('== TABUADA v3.0 =='))
print('=-='*23)
cont = 0
produto = 1
while True:
    num = int(input('>>Digite um número para ver sua tabuada: '))
    if num < 0:
        print('>>Programa Encerrado.')
        break
    while cont < 11:
        cont += 1
        produto = num * cont
        print(f'{num} x {cont} = {produto}')
    cont = 0
