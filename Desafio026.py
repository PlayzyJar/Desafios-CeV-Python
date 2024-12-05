nome = str(input('>>Digite uma frase: ')).strip().lower()
print('>>A letra A aparece {} vez(es) na frase'.format(nome.count('a')))
print('>>A primeira letra A aparece na posição {}'.format(nome.find('a')+1))
print('>>A última letra A aparece na posição {}'.format(nome.rfind('a')+1))
