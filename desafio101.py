from datetime import datetime

def voto(nascimento):
    idade = (datetime.now().year - nascimento)

    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA.')
    elif 16 == idade == 17:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    elif 18 <= idade <= 65:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    else:
        print(f'Com {idade} anos VOTO OPCIONAL.')

#Main App
ano =  int(input('Em que ano você nasceu? '))
voto(ano)
print()
