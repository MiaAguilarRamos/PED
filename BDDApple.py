import pandas as pd
import mysql.connector
from mysql.connector import Error


def TablasBG():
    try:
        datos = pd.read_csv("Datasets/apple_balance.csv")
        datos = datos.dropna()

        datos.replace('-', 0, inplace=True)

        for col in datos.columns[1:]:
            datos[col] = pd.to_numeric(datos[col], errors='coerce').fillna(0).astype(int)

        lista_valores = datos.values.tolist()

        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password='lkj4S!**',
            database="PPEDD"
        )

        if conexion.is_connected():
            print("Connectado a la base de datos")

        cursor = conexion.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Datos_Apple (
                Cuenta VARCHAR(100),
                `2024-31/03` INT,
                `2023-31/12` INT,
                `2023-30/09` INT,
                `2023-30/06` INT
            )
        """)


        cursor.executemany("""
            INSERT INTO Datos_Apple (Cuenta, `2024-31/03`, `2023-31/12`, `2023-30/09`, `2023-30/06`)
            VALUES (%s, %s, %s, %s, %s)
        """, lista_valores)


        conexion.commit()

        cursor.execute("SELECT * FROM Datos_Apple")
        resultado = cursor.fetchall()

        for fila in resultado:
            print(fila)

    except Error as e:
        print(f"Error: {e}")

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Concexion cerrada")


if __name__ =='__main__':
    TablasBG()
