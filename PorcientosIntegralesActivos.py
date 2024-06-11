import pandas as pd
import plotly.express as px
from dash import html, dcc, dash_table
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

def crear_conexion():
    try:
        conexion = create_engine('mysql+mysqlconnector://root:lkj4S!**@127.0.0.1/PPEDD')
        print("Conectado a la base de datos")
        return conexion
    except SQLAlchemyError as e:
        print(f"Error: {e}")
        return None

def obtener_datos_activos(conexion, tabla):
    query = f"SELECT * FROM {tabla}"
    df = pd.read_sql(query, conexion)

    total_activo_fila = df[df['Cuenta'] == 'Total activo']
    if total_activo_fila.empty:
        raise ValueError("La fila 'Total activo' no está presente en los datos")

    total_activo_valores = total_activo_fila.iloc[0, 1:].astype(float)

    activos_df = df[df.index < total_activo_fila.index[0]].copy()

    for col in activos_df.columns[1:]:
        activos_df.loc[:, f'{col}_porcentaje'] = activos_df[col] / total_activo_valores[col] * 100

    activos_df = pd.concat([activos_df, total_activo_fila])

    return activos_df

def dibujar_activos(data_spotify, data_apple):
    fig_spotify = px.line(data_spotify, x="Cuenta", y=[col for col in data_spotify.columns if 'porcentaje' in col],
                          title="Spotify Balance (Análisis Vertical)")
    fig_spotify.update_yaxes(dtick=5)

    fig_apple = px.line(data_apple, x="Cuenta", y=[col for col in data_apple.columns if 'porcentaje' in col],
                        title="Apple Balance (Análisis Vertical)")
    fig_apple.update_yaxes(dtick=5)

    body = html.Div([
        html.H2("Análisis Vertical del Balance Semanal - Activos", style={"textAlign": "center", "color": "blue"}),
        html.P("Análisis Vertical (porcientos integrales) de activos, dividiendo cada cuenta de activo entre el Total activo.",
               style={"color": "white"}),
        html.Hr(),
        dcc.Graph(figure=fig_spotify),
        dcc.Graph(figure=fig_apple),
        html.H3("Porcientos Integrales (Spotify)", style={"textAlign": "center", "color": "green"}),
        dash_table.DataTable(data=data_spotify.to_dict("records"), page_size=10),
        html.H3("Porcientos Integrales (Apple)", style={"textAlign": "center", "color": "red"}),
        dash_table.DataTable(data=data_apple.to_dict("records"), page_size=10)
    ], style={"background": "black"})
    return body