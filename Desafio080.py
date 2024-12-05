valores = list()
for c in range(0, 5):
    n = int(input('>>Digite um valor: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print('>>Valor adicionado ao fim da lista.')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'>>Valor adicionado na {pos+1}° posição.')
                break
            pos += 1
print('>>Os valores adicionados  foram: ', end='')
for p, num in enumerate(valores):
    if p < len(valores)-1:
        print(valores[p], end=', ')
    else:
        print(valores[p])
