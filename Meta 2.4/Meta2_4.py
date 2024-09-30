from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import time

def scrape_amazon(search_kw, num_pages):
    # Camino del driver
    driver_path = "C:\\Users\\tecol\\Documents\\chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

    # URL de AMAZON
    base_url = "https://www.amazon.com.mx/s?k="
    search_kw = search_kw.replace(" ", "+")

    laptop_title = []
    laptop_price = []
    laptop_delivery = []
    laptop_rating = []

    for page_num in range(1, num_pages + 1):
        # URL de búsqueda con paginación
        full_url = f"{base_url}{search_kw}&page={page_num}&__mk_es_MX=ÅMÅŽÕÑ&crid=14LUIQC5LKV5U&sprefix={search_kw}%2Caps%2C185&ref=nb_sb_noss_1"
        driver.get(full_url)
        time.sleep(5)  # Permitir que la página cargue

        page = BeautifulSoup(driver.page_source, 'html.parser')

        # Corrección en la selección de elementos
        for laptop in page.find_all('div', attrs={'data-component-type': 's-search-result'}):
            title = laptop.find('h2', attrs={'class': 'a-size-mini a-spacing-none a-color-base s-line-clamp-4'})
            if title:
                laptop_title.append(title.text)
            else:
                laptop_title.append('')

            price = laptop.find('span', attrs={'class': 'a-price-whole'})
            if price:
                # Limpiar el texto del precio
                clean_price = price.text.replace(',', '').replace('.', '')
                laptop_price.append(float(clean_price))
            else:
                laptop_price.append('')

            delivery = laptop.find('span', attrs={'class': 'a-text-bold'})
            if delivery:
                laptop_delivery.append(delivery.text)
            else:
                laptop_delivery.append('')

            rating = laptop.find('span', attrs={'class': 'a-icon-alt'})
            if rating:
                laptop_rating.append(rating.text)
            else:
                laptop_rating.append('')

    laptop_list = pd.DataFrame({
        'TITLE': laptop_title,
        'PRICE': laptop_price,
        'DELIVERY DATE': laptop_delivery,
        'RATING': laptop_rating,
    })

    laptop_list.to_csv(r"C:\Users\tecol\Documents\Python CD\Meta 2.4\Meta2_4.csv", index=False, header=True, encoding='utf-8-sig')

    print(laptop_list)

    # Cerrar el navegador
    driver.quit()

# Ejemplo de uso
scrape_amazon("laptop asus", 3)
