import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def datos_apple():
    driver = ChromeDriverManager().install()
    s = Service(driver)
    opc = Options()
    opc.add_argument("--window-size=1020,1200")
    navegador = webdriver.Chrome(service=s, options=opc)
    navegador.get("https://mx.investing.com/equities/apple-computer-inc-balance-sheet")
    time.sleep(10)

    soup = BeautifulSoup(navegador.page_source, "html5lib")
    tabla = soup.find("table", attrs={"class": "noHover"})

    datosDiccionario = {
        "Cuenetas": [],
        "2024/300-03": [],
        "2023/30-12": [],
        "2023/30-09": [],
        "2023/01-07": []
    }

    for row in tabla.find_all("tr")[1:]:
        valores = row.find_all("td")
        datosDiccionario["Total de activos corrientes"].append(valores[0].text)
        datosDiccionario["2024/300-03"].append(valores[1].text)
        datosDiccionario["2023/30-12"].append(valores[2].text)
        datosDiccionario["2023/30-09"].append(valores[3].text)
        datosDiccionario["2023/01-07"].append(valores[4].text)

    df = pd.DataFrame(datosDiccionario)
    df.to_csv("datasets/apple.csv")
    time.sleep(5)
    navegador.close()

if __name__ == "__main__":
    datos_apple()
