
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

def obtener_datos_pasivos(conexion, tabla):
    query = f"SELECT * FROM {tabla}"
    df = pd.read_sql(query, conexion)

    total_pasivo_fila = df[df['Cuenta'] == 'Total pasivo']
    if total_pasivo_fila.empty:
        raise ValueError("La fila 'Total pasivo' no está presente en los datos")

    total_pasivo_valores = total_pasivo_fila.iloc[0, 1:].astype(float)

    inicio_pasivos = df[df['Cuenta'] == 'Total pasivos corrientes'].index[0]
    fin_pasivos = total_pasivo_fila.index[0]

    pasivos_df = df.iloc[inicio_pasivos:fin_pasivos + 1].copy()

    for col in pasivos_df.columns[1:]:
        pasivos_df[col] = pasivos_df[col].astype(float)
        pasivos_df[f'{col}_porcentaje'] = (pasivos_df[col] / total_pasivo_valores[col]) * 100

    return pasivos_df

def dibujar_pasivos(data_spotify, data_apple):
    fig_spotify = px.line(data_spotify, x="Cuenta", y=[col for col in data_spotify.columns if 'porcentaje' in col],
                          title="Spotify Balance (Análisis Vertical)")
    fig_spotify.update_yaxes(dtick=5)

    fig_apple = px.line(data_apple, x="Cuenta", y=[col for col in data_apple.columns if 'porcentaje' in col],
                        title="Apple Balance (Análisis Vertical)")
    fig_apple.update_yaxes(dtick=5)

    body = html.Div([
        html.H2("Análisis Vertical del Balance Semanal - Pasivos", style={"textAlign": "center", "color": "blue"}),
        html.P("Análisis Vertical (porcientos integrales) de pasivos, dividiendo cada cuenta de pasivo entre el Total pasivo.",
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