import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, dash_table
import mysql.connector
from mysql.connector import Error


def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password='1234',
            database="PPEDD"
        )
        if conexion.is_connected():
            print("Conectado a la base de datos")
        return conexion
    except Error as e:
        print(f"Error: {e}")
        return None


def obtener_datos(conexion, tabla):
    query = f"SELECT * FROM {tabla}"
    df = pd.read_sql(query, conexion)

    # Encontrar la fila del "Total activo"
    total_activo_fila = df[df['Cuenta'] == 'Total activo']
    if total_activo_fila.empty:
        raise ValueError("La fila 'Total activo' no está presente en los datos")

    # Extraer los valores de "Total activo"
    total_activo_valores = total_activo_fila.iloc[0, 1:].astype(float)

    # Filtrar las filas de activos (antes de "Total activo")
    activos_df = df[df.index < total_activo_fila.index[0]]

    # Calcular el porcentaje integral (análisis vertical)
    for col in activos_df.columns[1:]:
        activos_df[f'{col}_porcentaje'] = activos_df[col] / total_activo_valores[col] * 100

    # Añadir la fila de "Total activo" de vuelta al DataFrame
    activos_df = pd.concat([activos_df, total_activo_fila])

    return activos_df


def dibujar(data_spotify: pd.DataFrame, data_apple: pd.DataFrame):
    # Crear gráficos
    fig_spotify = px.line(data_spotify, x="Cuenta", y=[col for col in data_spotify.columns if 'porcentaje' in col],
                          title="Spotify Balance (Análisis Vertical)")
    fig_spotify.update_yaxes(dtick=5)  # Ajustar la escala vertical a 5 en 5

    fig_apple = px.line(data_apple, x="Cuenta", y=[col for col in data_apple.columns if 'porcentaje' in col],
                        title="Apple Balance (Análisis Vertical)")
    fig_apple.update_yaxes(dtick=5)  # Ajustar la escala vertical a 5 en 5

    titulo = "Análisis Vertical del Balance Semanal"
    body = html.Div([
        html.H2(titulo, style={"textAlign": "center", "color": "blue"}),
        html.P(
            "A continuación se muestra el Análisis Vertical (también conocido como porcientos integrales), el cual consiste en dividir cada una de las cuentas de activo entre el Total activo.",
            style={"color": "white"}  # Cambiar el color de la letra a blanco
        ),
        html.Hr(),
        dcc.Graph(figure=fig_spotify),
        dcc.Graph(figure=fig_apple),
        html.H3("Porcientos Integrales (Spotify)", style={"textAlign": "center", "color": "green"}),
        dash_table.DataTable(data=data_spotify.to_dict("records"), page_size=10),
        html.H3("Porcientos Integrales (Apple)", style={"textAlign": "center", "color": "red"}),
        dash_table.DataTable(data=data_apple.to_dict("records"), page_size=10)
    ], style={"background": "black"})
    return body


if __name__ == "__main__":
    conexion = crear_conexion()
    if conexion:
        try:
            data_spotify = obtener_datos(conexion, "Tabla_Spotify")
            data_apple = obtener_datos(conexion, "Tabla_Apple")

            app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
            app.layout = dibujar(data_spotify, data_apple)
            app.run(debug=True)
        finally:
            if conexion.is_connected():
                conexion.close()
                print("Conexión cerrada")
