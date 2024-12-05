print('=-='*21, '\n', '{:^60}'.format('>>Detector de Palíndromos<<'))
print('=-='*21)
esarf = ''
frase = str(input('>>Digite uma palavra ou frase: ')).upper()
frases = frase.split()
frasej = ''.join(frases)
for c in range(len(frasej), 0, -1):
    esarf += frasej[c-1]
print('>>A palavra/frase {} escrita ao contrário fica {}'.format(frasej, esarf))
if frasej == esarf:
    print('>>{} é um PALÍNDROMO!'.format(frase))
elif frasej != esarf:
    print('>>{} NÃO É UM PALÍNDROMO!'.format(frase))
