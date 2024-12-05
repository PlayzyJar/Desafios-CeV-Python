print('', '-=-'*20, '\n            >>Analizador de Triângulos v2.0<<\n', '-=-'*20)
r1 = int(input('>>Primeira reta: '))
r2 = int(input('>>Segunda reta: '))
r3 = int(input('>>Terceira reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    if r1 == r2 and r2 == r3:
        print('>>As retas PODEM formar um triângulo EQUILÁTERO.')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('>>As retas PODEM formar um triângulo ESCALENO.')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
        print('>>As retas PODEM formar um triângulo ISÓSCELES.')
else:
    print('>>As retas NÃO podem formar um triângulo.')
