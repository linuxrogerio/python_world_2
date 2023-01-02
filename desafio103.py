def ficha(jog='<Desconhecido>', gol=0):
    print(f'Jogador {jog} fez {gol} gol(s) no campeonato.')


#Main App
n = str(input('Nome do Jogador: '))
g = str(input('Número de gols:' ))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
