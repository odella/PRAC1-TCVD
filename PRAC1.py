#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Importem llibreries necessaries
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from datetime import date

# Separem el link en 2 parts. Al mitg utilitzarem un integer per iterar.
link = "https://www.capraboacasa.com/portal/es/super/ofertas/oferta/2001?nuevaPagina="
endlink = "&sort=promocionado%20asc,%20importeVentasProducto%20desc"

# Iniciem les llistes a omplir.
names = []
prices = []
deals = []
ids = []

# Iniciem sessió
session = requests.Session()

# Creem un semàfor per a controlar el bucle while
semafor = True

# Inicialitzem i per a iterar la web
i = 1

# Utilitzem el bucle while per a seguir descarregant dades mentres en 
# disposem de noves.
while semafor:
    
    # Variable de control del bucle.
    arr_len = len(names)

    # Descarreguem les dades
    result = session.get(link + str(i) + endlink)
    src = result.content
    soup = BeautifulSoup(src, features="html.parser", from_encoding='latin-1')

    # Primer extraiem els tags d'oferta
    for price_cell in soup.find_all("div", {
        'class': ['product col s6 m3 l3 small-product', "product col s6 m3 l3 small-product disabled"]}):
        cell_soup = BeautifulSoup(str(price_cell), features="html.parser")
        ids.append(price_cell.get("data-productid"))
        
        # Com que cada oferta pot tenir entre 0-3 categories, les guardem
        # en arrays.
        offers = []
        for deal in cell_soup.find_all("img", {'class': 'responsive-img tooltipped'}):
            
            # Utilitzem la funció get de l'objecte de tipus tag per aconseguir
            # la informació sobre l'oferta.
            deal_tag = deal.get("alt")
            offers.append(deal_tag.encode('latin-1').decode('utf-8'))
        
        deals.append(offers)

    # Extraiem el nom del producte
    for productName in soup.find_all("div", {'class': 'ellipsis multiline'}):
        name = productName.text
        names.append(name.encode('latin-1').decode('utf-8'))

    # Extraiem el preu
    for productPrice in soup.find_all("div", {'class': 'product-price'}):
        price = productPrice.text
        prices.append(price.encode('latin-1').decode('utf-8'))
    
    # Augmentem i en 1 per a seguir iterant la web.
    i = i+1
    
    # Si no hem aconseguit nova informació, tanquem el bucle while.
    if arr_len == len(names):
        semafor = False

# Obtenim la data per a introduirla al dataset com a variable i al nom.
date = date.today()
today = date.strftime("%d_%m_%Y")

# Creem, anomenem i desem el dataset.
df = pd.DataFrame({'Nom': names, 'ID Producte': ids, 'Preu': prices, 'Promocions': deals, 'Data': today})
file_name = "ofertesCaprabo_" + str(today) + ".csv"
df.to_csv(file_name, sep=';', index=False)


# In[ ]:




