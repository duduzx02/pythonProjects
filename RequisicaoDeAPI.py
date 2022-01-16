import requests

link = 'http://192.168.0.15:5000/'

requisicao = requests.get(link)

print(requisicao)
print(requisicao.json())

dicionario = requisicao.json()

print(dicionario['Total vendas'])