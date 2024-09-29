# Christopher Saul Hernandez Ramos
# Grupo 382

# Librerias
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

# Opciones de Firefox
options = Options()

# Inicializa el servicio de GeckoDriver
driver_path = r"C:\Users\tecol\Desktop\Python CD\geckodriver.exe"
service = Service(driver_path)

# Istancia para Firefox
driver = webdriver.Firefox(service=service, options=options)

# inicia el navegador
driver.fullscreen_window()
driver.get('https://www.amazon.com.mx/')
time.sleep(3)

driver.save_screenshot("P1.png")

# Buscador
search = driver.find_element("id", "twotabsearchtextbox")
search.send_keys("Nier")
search.send_keys(Keys.RETURN)
time.sleep(3)

driver.save_screenshot("P2.png")

# Seleccion de producto mediante texto de enlace
try:
    link = driver.find_element(By.LINK_TEXT, "Nier Replicant Ver.1.22474487139... - PlayStation 4")
    link.click()
    time.sleep(3)
    driver.save_screenshot("P3.png")

    link2 = driver.find_element(By.LINK_TEXT,"Promociones")
    link2.click()
    time.sleep(3)
    driver.save_screenshot("P4.png")

except Exception as e:
    print(f"No se pudo encontrar el enlace: {e}")

# Buscador
search = driver.find_element("id", "twotabsearchtextbox")
search.send_keys("Transformer War for Cybertron")
search.send_keys(Keys.RETURN)
driver.save_screenshot("P5.png")



    
