from bs4 import BeautifulSoup

import requests

URL = input('digite o site')
site = requests.get("URL").content

soup = BeautifulSoup(site,'html.parser')

#print(soup.prettify())


caminho = #Essa variavel deve receber a tag do que deve ser pesquisado no site
temperatura = soup.find(caminho)
print(temperatura.string)

