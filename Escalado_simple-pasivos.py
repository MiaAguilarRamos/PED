import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, dash_table
def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password='',
            database="PPEDD"
        )
        if conexion.is_connected():
            print("Conectado a la base de datos")
        return conexion
    except Error as e:
        print(f"Error: {e}")
        return None

def obtener_datos(conexion, tabla):
    query = "SELECT * FROM {tabla}"
    df = pd.read_sql(query, conexion)

    # Encontrar la fila del "Total activo"
    total_pasivo_fila = df[df['Cuenta'] == 'Total Pasivo']
    if total_pasivo_fila.empty:
        raise ValueError("La fila 'Total Pasivo' no está presente en los datos")

    # Extraer los valores de "Total Paivoivo"
    total_Pasivo_valores = total_pasivo_fila.iloc[0, 1:].astype(float)

    # Filtrar las filas de activos (antes de "Total Pasivo")
    activos_df = df[df.index < total_pasivo_fila.index[0]]

    # Calcular el porcentaje integral (análisis vertical)
    for col in activos_df.columns[1:]:
        activos_df[f'{col}_porcentaje'] = pasivo_df.max[col] / total_pasivo_valores.max[col]

    # Añadir la fila de "Total pasivo" de vuelta al DataFrame
    activos_df = pd.concat([activos_df, total_pasivo_fila])

    return activos_df

def dibujar(data_spotify: pd.DataFrame, data_apple: pd.DataFrame):
    # Crear gráficos
    fig_spotify = px.line(data_spotify, x=" Pasivo Totales", y=[col for col in data_spotify.columns if 'Empresa' in col],
                          title="Spotify Balance _Escalado Simple-")
    fig_spotify.update_yaxes(dtick=5)  # Ajustar la escala vertical a 5 en 5

    fig_apple = px.line(data_apple, x="Pasivo Totales", y=[col for col in data_apple.columns if 'Empresa' in col],
                        title="Apple Balance -Escalado Simple-")
    fig_apple.update_yaxes(dtick=5)  # Ajustar la escala vertical a 5 en 5

    titulo = "Escalado Simple de Pasivo Totales"
    body = html.Div([
        html.H2(titulo, style={"textAlign": "center", "color": "blue"}),
        html.P(
            "Escalado simple de Pasivo Totales",
            style={"color": "white"}  # Cambiar el color de la letra a blanco
        ),
        html.Hr(),
        dcc.Graph(figure=fig_spotify),
        dcc.Graph(figure=fig_apple),
        html.H3("Pasivos Totales(Spotify)", style={"textAlign": "center", "color": "green"}),
        dash_table.DataTable(data=data_spotify.to_dict("records"), page_size=10),
        html.H3("Pasivos Totales (Apple)", style={"textAlign": "center", "color": "red"}),
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




