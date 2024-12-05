cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('>>Digite um número de 0 à 20: '))
    while n not in range(0, 21):
        n = int(input('>>O valor digitado è inválido! Tente novamente: '))
    print(f'>>Você digitou o número {cont[n]}')
    res = str(input('>>Começar denovo? [S/N]: ')).lower().strip()[0]
    if res not in 's':
        break
print('\n>>Extensor de números finalizado.')
