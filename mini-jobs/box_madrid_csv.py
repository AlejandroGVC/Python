#Ejercicio 3
#Descargar y parsear la página de Madrid en la wikipedia
#Extraer el infobox de madrid y meterlo en un csv
#Para crear el CSV vamos a quedarnos solo con los links dentro del infobox:
#El CSV tiene que tener 3 columnas: description, link, imagen (true o false)
#Filtrando los links hay que contruir dicho CSV, la columna imagen tiene que
#ser True cuando el link apunte a alguna imagen of False en caso contrario

import urllib3
from bs4 import BeautifulSoup
import re 
import pandas as pd

url = 'https://es.wikipedia.org/wiki/Madrid'

def get_html(url):
    
    url = url
    requests = urllib3.PoolManager()
    request = requests.request('GET', url)
    contenido = request.data
    pagina = BeautifulSoup(contenido, 'lxml')
    
    return pagina

def get_df(url):

    infobox = get_html(url).find('table', {'class':'infobox geography vcard'})
    links = infobox.find_all('a')

    ls_links = []
    ls_description = []
    ls_image = []

    for link in links:
        ls_links.append('https://es.wikipedia.org/' + link.get('href'))
        ls_description.append(link.get('title'))
        if link.get('class') == ['image']:
            ls_image.append('True')
        else:
            ls_image.append('False')

    df = pd.DataFrame(list(zip(ls_links, ls_description, ls_image)), 
                   columns =['Links', 'Description', 'Image']) 
    return df 

def create_csv(url):
    
    get_df(url).to_csv('wikimadrid.csv', index = False)   

create_csv(url)