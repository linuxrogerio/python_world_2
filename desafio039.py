print('########## Desafio 039 ##########')

import datetime

data = datetime.date.today()
#import pdb;pdb.set_trace() #debugging
ano_atual = data.year

ano_nascimento = int(input('\n Digite o ano do seu nascimento: '))

idade =  ano_atual - ano_nascimento
tempo_que_passou = idade - 18
tempo_que_falta = 18 - idade

if idade == 18:
    print('É hora de se alistar no serviço militar! \n')
    print('Se aliste agora! \n')
elif idade < 18:
    print('Você ainda irá se alistar no serviço militar! \n')
    print('Faltam {} anos para você se apresentar! \n'.format(tempo_que_falta))
elif idade > 18:
    print('\nJá passou do tempo de você se alistar no seviço militar! \n')
    print('Você passou {} anos do tempo regular para se apresentar! \n'.format(tempo_que_passou))