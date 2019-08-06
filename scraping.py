import requests
from bs4 import BeautifulSoup

url = 'https://pre.ufcg.edu.br:8443/ControleAcademicoOnline/Controlador?command=AlunoTurmasListar'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for tags in html.select('.container panel panel-primary text-center'):
    print(tags)