import requests
import pandas as pd
from bs4 import BeautifulSoup


def iniciar_extraccion():
    url = "https://mx.investing.com/equities/apple-computer-inc-balance-sheet"
    cabeceras_http = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    respuesta = requests.get(url, headers=cabeceras_http)

    if respuesta.status_code == 200:
        sopa = BeautifulSoup(respuesta.content, "html5lib")

        # Encuentra la tabla de balance
        tabla = sopa.find("table", attrs={"class": "genTbl reportTbl"})

        if not tabla:
            raise Exception("No se encontró la tabla de balance.")

        # Extrae las cabeceras
        cabeceras = [th.text.strip() for th in tabla.find_all("th")]
        print("Cabeceras encontradas:", cabeceras)

        # Extrae las filas de datos
        filas = []
        for tr in tabla.find_all("tr")[1:]:  # Saltamos el encabezado
            celdas = tr.find_all("td")
            fila = [celda.text.strip() for celda in celdas]
            filas.append(fila)

        # Visualiza algunas filas
        for fila in filas[:5]:
            print(fila)

        filas_validas = [fila for fila in filas if len(fila) == len(cabeceras)]

        # Creacion de un DataFrame
        df = pd.DataFrame(filas_validas, columns=cabeceras)
        print(df.sample(10))
        df.to_csv("datasets/apple_balance.csv", index=False)
    else:
        raise Exception("Ocurrió un error al hacer la solicitud HTTP!")


if __name__ == "__main__":
    iniciar_extraccion()


