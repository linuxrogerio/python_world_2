import requests as req

link = 'https://myapi.rogerioreis2.repl.co/pegarvendas'

requisicao = req.get(link)

print(requisicao)
print(requisicao.json())