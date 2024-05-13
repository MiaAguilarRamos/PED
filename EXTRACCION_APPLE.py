import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium .webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup




def datos_apple():
    driver = ChromeDriverManager()
    s = Service(driver.install())
    opc = Options()#objeto para agregar argumentos
    opc.add_argument("--window-size= 1020,1200")
    navegador = webdriver.Chrome(service=s, options=opc)
    navegador.get("https://mx.investing.com/equities/apple-computer-inc")
    time.sleep(10)


if __name__ == "__main__":
    datos_apple()









