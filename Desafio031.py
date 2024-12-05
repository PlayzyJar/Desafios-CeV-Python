km = int(input('        >>>Preço da Passagem<<< \n>>Qual a distância da viagem? '))
if km <= 200:
    print('>>Sua passagem irá custar R${:.2f}'.format(km*0.50))
    res1 = str(input('>>Vai querer a passagem senhor(a)? ')).strip().lower()
    if res1 == 'sim':
        print('>>Obrigado senhor(a)\n>>Boa viagem!')
    else:
        print('Ok, tenha um bom dia!')
else:
    print('>>Para viagens acima de 200Km você recebe 10%off')
    print('>>Sua passagem irá custar R${:.2f}'.format(km * 0.45))
    res1 = str(input('>>Vai querer a passagem senhor(a)? ')).strip().lower()
    if res1 == 'sim':
        print('>>Obrigado senhor(a)\n>>Boa viagem!')
    else:
        print('Ok, tenha um bom dia!')
