def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas e situações de vários alunos. 
    :param sit: valor opcional, indicando se deve ou não adicionar a situação. 
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL!'
        else:
            r['situacao'] = 'RUIM'
    return r


#Main App
resp = notas(4, 1, 5.5, 5.5, 6.5, sit=True)
#print(resp)
help(notas)