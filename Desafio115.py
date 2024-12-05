from time import sleep
from Exercicio115.lib.interface import *
from Exercicio115.lib.arquivo import *
m = ['Listar Pessoas Cadastradas', 'Cadastrar uma nova pessoa', 'Sair do Programa']

arq = 'SalaInfo1°A'

if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    res = menu(m)
    if res == 1:
        lerArquivo(arq)
    elif res == 2:

        cabecalho('>> NOVO CADASTRO <<')
        nome = str(input(' >>\033[1;34mNome: \033[m'))
        idade = LeiaInt(' >>\033[1;34mIdade: \033[m')
        cadastrar(arq, nome, idade)
    elif res == 3:
        linha()
        print('>>\033[1;34mEncerrando', end='')
        sleep(0.5)
        for c in range(0, 3):
            print('.', end='')
            sleep(1)
        print('\033[m\n>>\033[1;34mPrograma encerrado, até a próxima! :).')
        break
    else:
        print('\033[1;31m>>Opção inválida! Tente novamente!\033[m')
