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
    navegador.get("https://mx.investing.com/equities/apple-computer-inc-balance-sheet")
    time.sleep(10)
    #4 fechas-una de cuentas
    cuentas=navegador.find_element(By.NAME,"child")#tr
    periodo=navegador.find_element(By.NAME,"child")#td
#<div id="rrtable">==$0  ------------saca la tabla completa
    #ciclo para ubicar tr y luego metelo en con un td

    nAño=periodo.find_elements(By.TAG_NAME,"alignBottom")
    c=cuentas.find_element(By.TAG_NAME,"vertial-again: unherit")
    datosDiccionario={"Total de activos corrientes":[""],"2024/\n300-03":[],"2023/\n30-12":[],"2023/\n30-09":[],"2023/\n01-07":[],}

    for c in cuentas[1:]:#tr
        for nAño in periodo[-1:-6:-1]:#td
            soup=BeautifulSoup(navegador.page_source,"html5lib")#soup es el ue permite extraer el codigo html
            tabla=soup.find("table",attrs={"class":"noHover"})#especifica que tio de tabla quiere la info
            renglones=tabla.findAll("tr")
        for row in renglones[1:]:
            valores=row.findAll("td")
            datosDiccionario["Total de activos corrientes"].append(valores[0])
            datosDiccionario["2024/\n300-03"].append(valores[1])
            datosDiccionario["2023/\n30-12"].append(valores[2])
            datosDiccionario["22023/\n30-09"].append(valores[3])
            datosDiccionario["2023/\n01-07"].append(valores[4])


    df=pd.DataFrame(datosDiccionario)
    df.to_csv("datasets/apple.csv")#ruta de donde sera
    time.sleep(5)
    navegador.close()
            print(nAño.text)
            print(c.text)
if __name__=="__main__":
    datos_apple()