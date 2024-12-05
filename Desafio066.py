soma = cont = 0
while True:
    num = int(input('>>Digite um número: \n[999] Para parar\n>>Número: '))
    if num == 999:
        break
    soma += num
    cont += 1
    print('=-='*20)
print(f'>>Foram digitados {cont} números e a soma entre eles é {soma}')
