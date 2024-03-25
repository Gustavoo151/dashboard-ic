from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from components import cidades

from app import app


# ========== Layout ==========
layout = dbc.Col([
    html.H1("Baixo Peso ao nascer (BPN)", className='text-Dash'),
    html.P("By Gustavo Oliveira", className='text-info'),
    html.Hr(),


    # ========== Navegação Da Pages ==========
    dbc.Col([
        dbc.Nav([
            dbc.NavLink("Geral", href="/", active="exact"),
            dbc.NavLink("Cidades", href="/cidades", active="exact"),
            dbc.NavLink("Subgrupos", href="/subgrupos", active="exact"),
        ], vertical=True, pills=True, id='nav_buttons', style={'margin-botton': '50px'}),
        ], id='Sidebar-completa'),
])
