import pandas as pd
import mysql.connector
from mysql.connector import Error

def CreacionBDDSpotify():
    conexion = None
    try:

        datos = pd.read_csv("datasets/spotify_balance.csv")

        datos = datos.dropna()

        datos.replace('-', 0, inplace=True)


        for col in datos.columns[1:]:
            datos[col] = pd.to_numeric(datos[col], errors='coerce').fillna(0).astype(int)


        lista_valores = datos.values.tolist()

        # Conectar a la base de datos MySQL
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password='1234',
            database="BDDSpotify"
        )

        if conexion.is_connected():
            print("Conectado a la base de datos")

        cursor = conexion.cursor()

        # Crear la tabla si no existe
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS BG_Trime_Spotify (
                Cuenta VARCHAR(100),
                `2024-31/03` INT,
                `2023-31/12` INT,
                `2023-30/09` INT,
                `2023-30/06` INT
            )
        """)

        # Insertar los datos en la tabla
        cursor.executemany("""
            INSERT INTO BG_Trime_Spotify (Cuenta, `2024-31/03`, `2023-31/12`, `2023-30/09`, `2023-30/06`)
            VALUES (%s, %s, %s, %s, %s)
        """, lista_valores)

        # Confirmar los cambios
        conexion.commit()

        # Seleccionar y mostrar los datos insertados
        cursor.execute("SELECT * FROM BG_Trime_Spotify")
        resultado = cursor.fetchall()

        for fila in resultado:
            print(fila)

    except FileNotFoundError as e:
        print(f"Error: Archivo no encontrado - {e}")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conexion and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada")

if __name__ == '__main__':
    CreacionBDDSpotify()
