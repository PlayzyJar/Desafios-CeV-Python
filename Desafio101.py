def voto():
    from datetime import date
    idade = date.today().year - anonasc
    if idade in range(16, 18) or idade > 65:
        return print(f'>>Pessoas com {idade} anos tem VOTO OPCIONAL.')
    if idade < 16:
        return print(f'>>Pessoas com {idade} anos ou menos NÃO PODEM VOTAR.')
    if idade >= 18:
        return print(f'>>Pessoas com {idade} anos tem VOTO OBRIGATÓRIO.')


anonasc = int(input('>>Em que ano você nasceu? '))
print('{}=-={}'.format('\033[1;33m', '\033[m')*20)
voto()
