def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas e situações de vários alunos. 
    :param sit: valor opcional, indicando se deve ou não adicionar a situação. 
    :return: dicionário com várias informações sobre a situação da turma.
    """
    total = 0
    for i in range(0, len(n)):
        total += n[i]
        print(n[i])
    media = total / len(n)
    return media

resp = notas(5.5, 9.5, 6.5)
print(resp)