from random import shuffle
a1 = input('        >>>Ordem de Apresentação<<< \n>>Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('>>Terceiro aluno: ')
a4 = input('>>Quarto aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('>>A ordem de apresentação será: {}'.format(lista))
