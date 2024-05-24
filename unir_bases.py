import pandas as pd
import mysql.connector
from mysql.connector import Error


def TablasBG():
    try:
        datos = pd.read_csv("apple_balance.csv")
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
            CREATE TABLE IF NOT EXISTS BG_Trime_Apple (
                Cuenta VARCHAR(100),
                Primero INT,
                Segundo INT,
                Tercero INT,
                Cuarto INT
            )
        """)


        cursor.executemany("""
            INSERT INTO BG_Trime_Apple (Cuenta, Primero, Segundo, Tercero, Cuarto)
            VALUES (%s, %s, %s, %s, %s)
        """, lista_valores)


        conexion.commit()

        cursor.execute("SELECT * FROM BG_Trime_Apple")
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