cores = {0: '\033[m', 1: '\033[1;31m', 2: '\033[1;32m', 3: '\033[1;33m'}
dados = dict()
dados['Aluno'] = str(input('>>Nome do aluno: '))
dados['Média'] = float(input('>>Média do aluno: '))
print('=-='*13)
if dados['Média'] >= 7:
    dados['Situação'] = '{}Aprovado{}'.format(cores[2], cores[0])
elif 4.9 < dados['Média'] < 7:
    dados['Situação'] = '{}Recuperacão{}'.format(cores[3], cores[0])
else:
    dados['Situação'] = '{}Reprovado{}'.format(cores[1], cores[0])
print(' {:^16} | {:^5} | {:^8} '.format('Nome do Aluno', 'Média', 'Situação'))
print(' {:^16} | {:^5} | {:^10} '.format(dados['Aluno'], dados['Média'], dados['Situação']))
