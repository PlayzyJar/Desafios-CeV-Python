from random import choice
a1 = str(input('         >>>Sorteio na Lista<<< \n>>Nome do primeiro aluno: '))
a2 = str(input('>>Nome do segundo aluno: '))
a3 = str(input('>>Nome do terceiro aluno: '))
a4 = str(input('>>Nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
alunosr = choice(lista)
print('>>O aluno sorteado foi {}! '.format(alunosr))
