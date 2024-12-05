words = ('aprender', 'progrmar', 'linguagem', 'python',
         'curso', 'gratis', 'estudar', 'praticar',
         'trabalhar', 'mercado', 'programador', 'futuro')
for p in words:
    print(f'\n>>Na palavra {p.upper()} temos as vogais: ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
