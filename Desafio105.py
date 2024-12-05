def notas(*n, sit=False):
    """
    >>Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit: (opcional) Mostra a situação dos alunos.
    :return: Um dicionário informando os dados da turma.
    """
    r = dict()
    r['Total'] = len(n)
    r['Média'] = sum(n)/len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'Boa'
        elif r['Média'] >=5:
            r['Situação'] = 'Razoável'
        else:
            r['Situação'] = 'Ruim'
    return r


resp = notas(2, 10, 8, sit=True)
print(resp)
