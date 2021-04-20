#Ejercicio 3:
#Dada la página de noticias europeas del periodico EL PAIS (https://elpais.com/tag/europa/a/) 
#identificar para cada noticia el link que la expande y el titulo en portada.
#Por cada link identificado navegar a dicho link y extraer el titular y resumen
#Una vez conseguido lo anterior, modifique el código para que solo se navegue al link de la noticia 
#(y se procese) si su titulo en portada contiene un cierto keywork. Por ejemplo, ‘algas’ 

import urllib3
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://elpais.com/tag/europa/a/'

def get_html(url):
    
    url = url
    requests = urllib3.PoolManager()
    request = requests.request('GET', url)
    contenido = request.data
    pagina = BeautifulSoup(contenido, 'lxml')
    
    return pagina

def get_links(url):

    links = get_html(url).find_all('h2', {'class':'c_h'})
    ls_links = []

    for link in links:
        ls_links.append('https://elpais.com' + link.find('a').get('href'))

    return ls_links

def get_econ_news(url):
    
    titulos = []
    links = get_links(url)
    links_econ = []
    ls_titulos = []
    ls_resumen = []

    for link in links: 

        titulos.append(get_html(link).title.get_text())

    for i in range(0, len(titulos)):
        if 'Economía' in titulos[i]:
            links_econ.append(links[i])

    for link in links_econ:
        ls_titulos.append(get_html(link).find('div', {'class':'a_hg'}).find('h1', {'class':'a_t'}).get_text())
        ls_resumen.append(get_html(link).find('div', {'class':'a_hg'}).find('h2', {'class':'a_st'}).text)

    dict_final = {'Titulo': ls_titulos, 'Resumen': ls_resumen}
    data = pd.DataFrame(dict_final)
    
    print(data) 

    
get_econ_news(url)