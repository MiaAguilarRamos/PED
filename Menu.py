import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, dash_table
import PorcientosIntegralesActivos as activos
import PorcientosIntegralesPasivos as pasivos
import ComparacionTotales as comparacion

# Definir la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Aquí se colocan las páginas y su contenido
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
                dbc.NavLink("Comparación Activos y Pasivos", href="/comparacion", active="exact"),
                dbc.NavLink("Github", href="https://github.com/MiaAguilarRamos/PED", target="_blank", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style={"width": "20%", "position": "fixed", "top": 0, "left": 0, "bottom": 0, "padding": "20px",
           "background-color": "#f8f9fa"},
)

content = html.Div(id="page-content", style={"margin-left": "25%", "padding": "20px"})

# Para definir la forma en la que se acomoda la página, primero el menú y luego el contenido
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


# Actualizar el contenido de la página cada que se seleccione otra
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    conexion = activos.crear_conexion()
    if conexion:
        try:
            data_apple = activos.obtener_datos_activos(conexion, "Tabla_Apple")
            data_spotify = activos.obtener_datos_activos(conexion, "Tabla_Spotify")

            if pathname == "/":
                return html.P(
                    "En la siguiente página se puede acceder a la información obtenida sobre el balance general de las "
                    "empresas Spotify y Apple. De igual manera, en el menú de opciones se encuentran varios gráficos donde se "
                    "compara el comportamiento trimestral de las cuentas de ambas empresas para, en base a los resultados, "
                    "crear conclusiones o dar soporte a la toma de decisiones."
                )
            elif pathname == "/page-1":
                return html.Div([
                    html.H2("Balance General Apple", style={"textAlign": "center", "color": "blue"}),
                    dash_table.DataTable(data=data_apple.to_dict("records"), page_size=10)
                ])
            elif pathname == "/page-2":
                return html.Div([
                    html.H2("Balance General Spotify", style={"textAlign": "center", "color": "blue"}),
                    dash_table.DataTable(data=data_spotify.to_dict("records"), page_size=10)
                ])
            elif pathname == "/activos":
                return activos.dibujar_activos(data_spotify, data_apple)
            elif pathname == "/pasivos":
                data_spotify_pasivos = pasivos.obtener_datos_pasivos(conexion, "Tabla_Spotify")
                data_apple_pasivos = pasivos.obtener_datos_pasivos(conexion, "Tabla_Apple")
                return pasivos.dibujar_pasivos(data_spotify_pasivos, data_apple_pasivos)
            elif pathname == "/comparacion":
                # Filtrar las columnas que no contengan "_porcentaje"
                periodos = [col for col in data_apple.columns[1:] if "_porcentaje" not in col]
                return dbc.Container([
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


# Actualizar el gráfico de comparación
@app.callback(
    Output('grafico-comparacion', 'figure'),
    [Input('dropdown-periodo', 'value')]
)
def actualizar_grafico(periodo):
    conexion = activos.crear_conexion()
    if conexion:
        try:
            df_apple = comparacion.obtener_datos(conexion, "Tabla_Apple")
            df_spotify = comparacion.obtener_datos(conexion, "Tabla_Spotify")
            fig = comparacion.crear_grafico(df_apple, df_spotify, periodo)
            return fig
        finally:
            if conexion:
                conexion.dispose()


if __name__ == "__main__":
    app.run_server(debug=True, port=8054)