import re
import json
import urllib.request
import urlopen


url='https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
região = dados['region']

print('Detalhes do IP externo\n')
print('IP:{4}\nRegião: {1}\nPais: {2}\nCidade: {3}\nOrg.: {0}'. format(org, região, pais, cid, ip))
