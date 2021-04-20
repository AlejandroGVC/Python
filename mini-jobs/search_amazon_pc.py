# Ejercicio 5 
# Vamos a crear un scrapper al cual le pasamos una cadena de búsqueda, y este, 
# recuperará los resultados  desde amazon y pc componentes.
# Cada resultado encontrado se almacenará en un array con los siguientes elementos: 
# Amazon o PC componentes, el precio del producto, el nombre, y el link
# Al final de la búsqueda, imprimiremos los productos encontrados en ambas tiendas

import urllib3
from bs4 import BeautifulSoup
import pandas as pd

busqueda = str(input('Buscar producto:'))
url_amazon = str('https://www.amazon.es/s?k=' + busqueda) 
url_pc = str('https://www.pccomponentes.com/buscar/?query=' + busqueda)

def get_html_amazon(url_amazon):
    
    url = url_amazon
    requests = urllib3.PoolManager()
    request = requests.request('GET', url)
    contenido = request.data
    pagina = BeautifulSoup(contenido, 'lxml')
    
    return pagina

def get_html_pc(url_pc):
    
    url = url_pc
    requests = urllib3.PoolManager()
    request = requests.request('GET', url)
    contenido = request.data
    pagina = BeautifulSoup(contenido, 'lxml')
    
    return pagina    

def get_vars_pc(url_pc):

    products = get_html_pc(url_pc).find_all('div', {'class':'c-product-card__content'})
    ls_productos = []

    for product in products:
        
        empresa = 'PC Componentes'
        link = product.find('a', {'class':'c-product-card__title-link'}).get('href')
        name = product.find('a', {'class':'c-product-card__title-link'}).text
        price = product.find('a', {'class':'c-product-card__title-link'}).get('data-price')
        producto = str(empresa + ':' + name + ' ' + price + '€' + ' '  + link)
        ls_productos.append(producto)

    return ls_productos

def get_vars_amazon(url_amazon):

    try:
        products = get_vars_amazon(url_amazon).find_all('div', {'class':'a-section'})
        ls_productos = []

        for product in products:
            empresa = 'Amazon'
            link = product.find('a', {'class':'a-link-normal'}).get('href')
            name = product.find('span', {'class':'a-size-base-plus'}).text
            price = product.find('span', {'class':'a-price-whole'}).text
            producto = str(empresa + ':' + name + ' ' + price + '€' + ' '  + link)
            ls_productos.append(producto)

        
    except:
        ls_productos = 'baneado'

    return ls_productos

print(get_vars_pc(url_pc))
print(get_vars_amazon(url_amazon))