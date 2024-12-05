from Exercicio115.lib.interface import cabecalho


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'\033[1;31m>>Ocorreu algum erro ao criar o arquivo {nome}\033[m')
    else:
        print(f'>>\033[1;32mArquivo {nome} criado com sucesso!\033[m')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[1;31m>>Ocorreu um erro ao abrir o arquivo.')
    else:
        cabecalho('>> PESSOAS CADASTRADAS <<')
        for linha in a:
            dado = linha.split(';')
            print(f'{dado[0]:<37}{dado[1]:>3} anos'.replace('\n', ''))


def cadastrar(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[1;31m>>Ops... ocorreu um erro ao fazer o cadastro.\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[1;31m>>Ocorreu um erro ao escrever os dados.\033[m')
        else:
            print(f'>>\033[1;32mNovo cadastro de {nome} adicionado com sucesso!\033[m')
