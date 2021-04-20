# Ejercicio 1
#Descargar y parsear la página de Madrid en la wikipedia
#Imprimir por pantalla el titulo
#Extraer todos los links que pertenezcan a la wikipedia
#Navegar a todos aquellos que no sean imagenes (en realidad para evitar un volumen grande navegar solo a 4)
#Repetir el proceso de forma recurisiva, y/o iterativa ;)

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

def print_title(url):
    
    return get_html(url).title.get_text()

def wiki_link(url):
    
    expr_reg = re.compile('/wiki/[^\"]+')
    links = get_html(url).find_all(True, {'href':expr_reg})
    ls_links = []

    for link in links:
        ls_links.append(link.get('href'))
        
    return ls_links

def search_link(url):

    expr = re.compile('\.\w+$')
    
    ls_reduce_links = wiki_link(url)[0:4]
    
    # Este bucle usa la función expr.findall para quitar 
    # las imagenes. Y despues como los links vienen en
    # de forma diferente, los modifica para que todos
    # sean navegables

    for link in ls_reduce_links:
        if not expr.findall(link):
            if link.startswith('https:'):
                print(print_title(link) )
            elif link.startswith('/wiki/'):
                print(print_title('https://es.wikipedia.org' + link))
            else:
                print(print_title('https:' + link))

search_link(url)