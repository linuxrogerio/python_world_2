

def voto(nascimento):
    from datetime import datetime
    idade = (datetime.today().year - nascimento)
    print(idade)

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

#Main App
ano =  int(input('Em que ano você nasceu? '))
print(voto(ano))
print()
