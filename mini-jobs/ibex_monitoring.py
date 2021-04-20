# Ejercicio 4
# Dados los precios del Ibex35 publicados en yahoo finanzas 
# https://es.finance.yahoo.com/quote/%5EIBEX/
# Vamos a monitorizar el precio de cierre que aparece en la pestaña resumen.
# El código verificará las condiciones cada minuto.
# Definimos dos umbrales en nuestro código e imprimimos en pantalla para avisar a un usuario cuando:
# Si el cierre supera nuestro umbral 1 (llamémoslo máximo) 
# Si el cierre es inferior a nuestro umbral 2 (llamémoslo mínimo)

import urllib3
from bs4 import BeautifulSoup
import pandas as pd
import time

url = 'https://es.finance.yahoo.com/quote/%5EIBEX/'
maximo = 8600.0
minimo = 8595.0

def get_html(url):
    
    url = url
    requests = urllib3.PoolManager()
    request = requests.request('GET', url)
    contenido = request.data
    return BeautifulSoup(contenido, 'lxml')
    
    
def get_close(url):

	return get_html(url).find('span', {'class':'Trsdu(0.3s)'}).text


def float_value(url):

	 return float(get_close(url).replace('.', '').replace(',', '.'))


while True:
	localtime = time.localtime()
	current_time = time.strftime("%I:%M:%S %p", localtime)
	print(current_time)
	cierre = float_value(url)
	print(cierre)
	if cierre > maximo:
		print('El cierre ('+str(cierre)+') ha superado el maximo ('+str(maximo)+')')
	elif cierre < minimo:
		print('El cierre  ('+str(cierre)+') esta por debajo del minimo ('+str(minimo)+')')
	time.sleep(10)
	break