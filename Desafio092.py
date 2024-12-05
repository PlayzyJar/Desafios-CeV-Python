from datetime import date
dados = dict()
dados['Nome'] = str(input('>>Nome: '))
dados['Ano nasc.'] = int(input('>>Ano de nascimento: '))
dados['CTPS'] = int(input('>>N° da Carteira de Trabalho (0 caso não tiver): '))
if dados['CTPS'] == 0:
    print('=-='*18)
    print(f'>>Nome: {dados["Nome"]}')
    print(f'>>Idade: {date.today().year-dados["Ano nasc."]} anos.')
    print('>>CTPS: Não possui.')
else:
    dados['Ano Contr.'] = int(input('>>Ano de contratação: '))
    dados['SB'] = float(input('>>Salário Bruto Mensal: R$'))
    print('=-='*18)
    print(f'>>Nome: {dados["Nome"]}')
    print(f'>>Idade: {date.today().year - dados["Ano nasc."]} anos.')
    print(f'>>CTPS: {dados["CTPS"]}.')
    print(f'>>Salário: R${dados["SB"]:.2f}')
    print(f'>>Idade prevista para aposentadoria: {dados["Ano Contr."]-dados["Ano nasc."]+35} anos.')
