nofwomens = 0
nmoreold = ''
hmoreold = 0
somaid = 0
for c in range(1, 5):
    print('========== {}° Pessoa =========='.format(c))
    nome = str(input('>>Nome: '))
    idade = int(input('>>Idade: '))
    gen = str(input('>> Gênero [F/M]: ')).strip().lower()
    somaid += idade
    if gen == 'f' and idade < 20:
        nofwomens += 1
    if c == 1 and gen == 'm':
        hmoreold = idade
        nmoreold = nome
    if idade > hmoreold and gen == 'm':
        hmoreold = idade
        nmoreold = nome
mediaid = somaid / 4
print('='*31, '\n>>A média de idade desse grupo de pessoas é de {} anos.'.format(mediaid))
print('>>O homem mais velho deste grupo tem {} anos e se chama {}.'.format(hmoreold, nmoreold))
print('>>Ao todo são {} mulheres com menos de 20 anos.'.format(nofwomens))
