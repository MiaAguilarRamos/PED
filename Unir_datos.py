import pandas as pd
import mysql.connector
from mysql.connector import Error

def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password='lkj4S!**',
            database="PPEDD"
        )
        if conexion.is_connected():
            print("Conectado a la base de datos")
        return conexion
    except Error as e:
        print(f"Error: {e}")
        return None



def Crear_Tablas(conexion):
    try:

        datos = pd.read_csv("Datasets/spotify_balance.csv")

        datos = datos.dropna()

        datos.replace('-', 0, inplace=True)


        for col in datos.columns[1:]:
            datos[col] = pd.to_numeric(datos[col], errors='coerce').fillna(0).astype(int)


        lista_valores = datos.values.tolist()



        if conexion.is_connected():
            print("Conectado a la base de datos")

        cursor = conexion.cursor()

        # Crear la tabla si no existe
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Tabla_Spotify (
                Cuenta VARCHAR(100),
                `2024-31/03` INT,
                `2023-31/12` INT,
                `2023-30/09` INT,
                `2023-30/06` INT
            )
        """)

        # Insertar los datos en la tabla
        cursor.executemany("""
            INSERT INTO Tabla_Spotify (Cuenta, `2024-31/03`, `2023-31/12`, `2023-30/09`, `2023-30/06`)
            VALUES (%s, %s, %s, %s, %s)
        """, lista_valores)

        # Confirmar los cambios
        conexion.commit()

        # Seleccionar y mostrar los datos insertados
        cursor.execute("SELECT * FROM Tabla_Spotify")
        resultado = cursor.fetchall()

        for fila in resultado:
            print(fila)

    except FileNotFoundError as e:
        print(f"Error: Archivo no encontrado - {e}")
    except Error as e:
        print(f"Error: {e}")

    try:
        datos = pd.read_csv("datasets/apple_balance.csv")
        datos = datos.dropna()

        datos.replace('-', 0, inplace=True)

        for col in datos.columns[1:]:
            datos[col] = pd.to_numeric(datos[col], errors='coerce').fillna(0).astype(int)

        lista_valores = datos.values.tolist()

        cursor = conexion.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Tabla_Apple (
                Cuenta VARCHAR(100),
                `2024-31/03` INT,
                `2023-31/12` INT,
                `2023-30/09` INT,
                `2023-30/06` INT
            )
        """)

        cursor.executemany("""
            INSERT INTO Tabla_Apple (Cuenta, `2024-31/03`, `2023-31/12`, `2023-30/09`, `2023-30/06`)
            VALUES (%s, %s, %s, %s, %s)
        """, lista_valores)

        conexion.commit()

        cursor.execute("SELECT * FROM Tabla_Apple")
        resultado = cursor.fetchall()

        for fila in resultado:
            print(fila)

    except Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    conexion = crear_conexion()
    if conexion:
        try:
            Crear_Tablas(conexion)

        finally:
            if conexion.is_connected():
                conexion.close()
                print("Conexión cerrada")