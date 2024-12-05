n = int(input('>>Digite o número do qual deseja ver a tabuada: '))
for t in range(1, 11):
    print('>>{} x {} = {}'.format(n, t, n*t))
