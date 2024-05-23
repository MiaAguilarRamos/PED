import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def datos_apple():
    driver = ChromeDriverManager()
    s = Service(driver.install())
    opc = Options()
    opc.add_argument("--window-size= 1020,1200")
    navegador = webdriver.Chrome(service=s, options=opc)
    navegador.get("https://mx.investing.com/equities/apple-computer-inc-balance-sheet")
    time.sleep(10)

    table = navegador.find_element(By.XPATH, "//table[@class='genTbl closedTbl crossRatesTbl elpTbl elp20']")

    html = navegador.page_source
    soup = BeautifulSoup(html, "html5lib")
    rows = table.find_elements(By.TAG_NAME, "tr")
    columns = [th.text for th in rows[0].find_elements(By.TAG_NAME, "th")]

    datosDiccionario = {column: [] for column in columns}

    for row in rows[1:]:
        cols = row.find_elements(By.TAG_NAME, "td")
        for i, col in enumerate(cols):
            datosDiccionario[columns[i]].append(col.text)

    df = pd.DataFrame(datosDiccionario)
    df.to_csv("datasets/apple.csv")

    time.sleep(5)
    navegador.close()

if __name__ == "__main__":
    datos_apple()