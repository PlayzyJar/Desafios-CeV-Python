nome = str(input('>>Qual seu nome completo? ')).strip().split()
print('>>Prazer em conhecê-lo \n>>Seu primeiro nome é {}'.format(nome[0]))
print('>>E o seu último nome é {}'.format(nome[len(nome)-1]))
