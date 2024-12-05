ipow = ['escudo', 'força bruta', 'martelo', 'inteligência', 'arco e flecha']
ivin = ['Capitão América', 'Hulk', 'Thor', 'Viúva Negra', 'Gavião Arqueiro']
# inow = '' caso tu precise dessa variável, tire a #, senão exclua essa linha

vin = str(input('Por favor, informe o vingador: ')).strip()
pow = str(input('Diga seu poder: ')).lower().strip()
ene = int(input('Informe sua energia: '))

if (vin in ivin) and (pow in ipow):
    for n, c in enumerate(ipow):
        if c == pow:
            if ivin[n] == vin:
                print('Tudo ok!')
                # aqui tu faz o os testes de poder e energia pra saber se ele pode ou não derrotar o Thanos
            else:
                #nesse caso aqui o pode não corresponde ao vingador
                print(f'Você disse {vin} , e esse poder é do(a) {ivin[n]}')
else:
    if vin not in ivin:
        print("Nome do vingador inválido!")
    if pow not in ipow:
        print("Poder de vingador inválido!")
