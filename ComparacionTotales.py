import pandas as pd
import plotly.express as px
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output
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

def obtener_datos(conexion, tabla):
    query = f"SELECT * FROM {tabla}"
    df = pd.read_sql(query, conexion)
    return df

def filtrar_datos(df, cuenta, periodo):
    return df.loc[df['Cuenta'] == cuenta, periodo].values[0]

def crear_grafico(df_apple, df_spotify, periodo):
    total_activos_apple = filtrar_datos(df_apple, 'Total activo', periodo)
    total_pasivos_apple = filtrar_datos(df_apple, 'Total pasivo', periodo)
    total_activos_spotify = filtrar_datos(df_spotify, 'Total activo', periodo)
    total_pasivos_spotify = filtrar_datos(df_spotify, 'Total pasivo', periodo)

    data = {
        'Cuenta': ['Total Activos', 'Total Pasivos'],
        'Apple': [total_activos_apple, total_pasivos_apple],
        'Spotify': [total_activos_spotify, total_pasivos_spotify]
    }

    df_comparacion = pd.DataFrame(data)

    fig = px.bar(df_comparacion, x='Cuenta', y=['Apple', 'Spotify'], barmode='group',
                 title=f'Comparación de Total Activos y Total Pasivos - {periodo}',
                 labels={'value': 'Valores', 'variable': 'Compañía'})

    fig.update_layout(
        xaxis_title="Cuenta",
        yaxis_title="Valores",
        legend_title="Compañía",
        legend=dict(x=0.8, y=1.15),
        barmode='group'
    )

    return fig

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

conexion = crear_conexion()
df_apple = obtener_datos(conexion, "Tabla_Apple")
df_spotify = obtener_datos(conexion, "Tabla_Spotify")
conexion.dispose()

periodos = df_apple.columns[1:].tolist()

app.layout = dbc.Container([
    html.H1("Comparación de Total Activos y Total Pasivos", className="mt-4"),
    dbc.Row([
        dbc.Col(
            dcc.Dropdown(
                id='dropdown-periodo',
                options=[{'label': periodo, 'value': periodo} for periodo in periodos],
                value=periodos[0],
                style={'width': '100%', 'margin-bottom': '20px'}
            ),
            width=3
        ),
        dbc.Col(
            dcc.Graph(id='grafico-comparacion'),
            width=9
        )
    ])
], fluid=True)

@app.callback(
    Output('grafico-comparacion', 'figure'),
    [Input('dropdown-periodo', 'value')]
)
def actualizar_grafico(periodo):
    fig = crear_grafico(df_apple, df_spotify, periodo)
    return fig
