import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, dash_table
import PorcientosIntegralesActivos as activos
import PorcientosIntegralesPasivos as pasivos
import pandas as pd

# Definir la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Aqui se colocan las paginas y su contenido
sidebar = html.Div(
    [
        html.H2("Menú", className="display-5"),
        html.Hr(),
        html.P("Seleccione una opción:", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Balance General Apple", href="/page-1", active="exact"),
                dbc.NavLink("Balance General Spotify", href="/page-2", active="exact"),
                dbc.NavLink("Porcientos Integrales - Activos", href="/activos", active="exact"),
                dbc.NavLink("Porcientos Integrales - Pasivos", href="/pasivos", active="exact"),
                dbc.NavLink("Github", href="https://github.com/MiaAguilarRamos/PED", target="_blank", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style={"width": "20%", "position": "fixed", "top": 0, "left": 0, "bottom": 0, "padding": "20px", "background-color": "#f8f9fa"},
)


content = html.Div(id="page-content", style={"margin-left": "25%", "padding": "20px"})

# Para definir la fomra en la que se acomoda la pagina, primero el menu y luego el contenido
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

def obtener_balance_general(conexion, tabla):
    query = f"SELECT * FROM {tabla}"
    df = pd.read_sql(query, conexion)
    return df

# Actualizar el contenido de la página cada que se seleccione otra
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    conexion = activos.crear_conexion()
    if conexion:
        try:
            if pathname == "/":
                return html.P(
                    "En la siguiente página se puede acceder a la información obtenida sobre el balance general de las "
                    "empresas Spotify y Apple. De igual manera, en el menú de opciones se encuentran varios gráficos donde se "
                    "compara el comportamiento trimestral de las cuentas de ambas empresas para, en base a los resultados, "
                    "crear conclusiones o dar soporte a la toma de decisiones."
                )
            elif pathname == "/page-1":
                data_apple = obtener_balance_general(conexion, "Tabla_Apple")
                return html.Div([
                    html.H2("Balance General - Apple", style={"textAlign": "center"}),
                    dash_table.DataTable(data=data_apple.to_dict("records"), page_size=10)
                ])
            elif pathname == "/page-2":
                data_spotify = obtener_balance_general(conexion, "Tabla_Spotify")
                return html.Div([
                    html.H2("Balance General - Spotify", style={"textAlign": "center"}),
                    dash_table.DataTable(data=data_spotify.to_dict("records"), page_size=10)
                ])
            elif pathname == "/activos":
                data_spotify = activos.obtener_datos_activos(conexion, "Tabla_Spotify")
                data_apple = activos.obtener_datos_activos(conexion, "Tabla_Apple")
                return activos.dibujar_activos(data_spotify, data_apple)
            elif pathname == "/pasivos":
                data_spotify = pasivos.obtener_datos_pasivos(conexion, "Tabla_Spotify")
                data_apple = pasivos.obtener_datos_pasivos(conexion, "Tabla_Apple")
                return pasivos.dibujar_pasivos(data_spotify, data_apple)
            else:
                return html.Div(
                    [
                        html.H1("404: No encontrado", className="text-danger"),
                        html.Hr(),
                        html.P(f"La ruta {pathname} no fue reconocida..."),
                    ],
                    className="p-3 bg-light rounded-3",
                )
        finally:
            if conexion:
                conexion.dispose()
                print("Conexión cerrada")


if __name__ == "__main__":
    app.run_server(debug=True, port=8054)