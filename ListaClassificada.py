numeros = []
chave = 0

for _ in range(5):
    numero = int(input())
    for chave, valor in enumerate(numeros):
        if numero < valor:
            numeros.insert(chave, numero)
            break
    else:
        numeros.append(numero)
        chave += 1

    if _ == 0 or chave == len(numeros)-1:
        print("valor adicionado no final da lista")

    else:
        print(f"valor adicionado na posição {chave} da lista")

print(numeros)
