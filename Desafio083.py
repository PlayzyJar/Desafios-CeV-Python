exp = str(input('>>Digite sua expressão: '))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        elif len(pilha) == 0:
            pilha.append('(')
            break
if len(pilha) == 0:
    print('>>Sua expressão está válida')
else:
    print('>>Essa expressão é inválida.')
