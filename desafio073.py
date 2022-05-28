print('{:=^40}'.format(' Desafio 073 '))


times = ("Palmeiras", "Santos", "Vasco da Gama", "Grêmio", "Flamengo",
         "Corinthians", "Internacional", "Cruzeiro", "São Paulo", "Atlético Mineiro",
         "Botafogo", "Fluminense", "Coritiba", "Bahia", "Goiás", "Guarani", "Sport",
         "Portuguesa", "Atlético Paranaense", "Vitória")

print('\n', '=-='*15)
print(f'\nOs 5 primeiro colocadodos são: {times[:5]}')

print('\n', '=-='*15)
print(f'\nOs 4 últimos colocados são: {times[-4:]}')

print('\n', '=-='*15)
print(f'\nOs times em ordem alfabética: {sorted(times)}')

print('\n', '=-='*15)
print(f'\nO Fluminense está na {times.index("Fluminense")}° posição.')
