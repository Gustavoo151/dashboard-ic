from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from components import sidebar, dashboards, geral, cidades

from app import *
from components import sidebar, dashboards, geral

# ========== Layout ==========
content = html.Div(id="page-content")

app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dcc.Location(id="url"),
            sidebar.layout
        ], md=2),
        dbc.Col([
            content
        ], md=10)
    ])
], fluid=True)

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def render_page_content(pathname):
    if pathname == '/' or pathname == '/dashboard':
        return dashboards.layout

    if pathname == '/geral':
        return geral.layout

    if pathname == '/cidades':
        return cidades.layout

    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

if __name__ == '__main__':
    app.run_server(debug=True)