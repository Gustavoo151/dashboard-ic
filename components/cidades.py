from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from app import app

# Texto com porcentagem de crianças com baixo peso na cidade
df = pd.read_csv('./Data/RID_DM_peso_familia_410750_WRAccAND_sim0.4k10ks2.csv')




# ========== Layout ==========
layout = dbc.Col([

    dbc.Row([
       html.Div(id='porcentage_cidade_output', style={'margin-left': '60px', 'margin-top': '80px'})
    ])

])
