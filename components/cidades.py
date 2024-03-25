import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import json
from app import app
import Data
import requests

# Texto com porcentagem de crianças com baixo peso na cidade
df = pd.read_csv('./Data/RID_DM_peso_familia_410750_WRAccAND_sim0.4k10ks2.csv')

# # Exemplo de uso de Dash mapa
df_states = pd.read_csv("./Data/df_states.csv")
df_brasil = pd.read_csv("./Data/df_brasil.csv")
df_states_ = df_states[df_states["data"] == "2020-05-13"]
brasil_states = json.load(open("./Data/brazil_geo.json", "r"))
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
fig = px.choropleth_mapbox(df_states_, locations='estado', color='casosNovos',
                           center={"lat": -14.24, "lon": -53.18}, zoom=3,
                           geojson=brasil_states, color_continuous_scale="blues", opacity=0.6,
                           hover_data={"casosAcumulado": True, "casosNovos": True, "obitosNovos": True, "estado": True})
fig.update_layout(
    paper_bgcolor="#ffffff",
    autosize=True,
    margin=go.layout.Margin(l=0, r=0, t=0, b=0),
    showlegend=False,
    mapbox_style="carto-positron",
    dragmode='lasso',
    coloraxis_showscale=False,
)

# Mostrando dados da cidade
# Fazendo a requisição
link = "https://servicodados.ibge.gov.br/api/v3/agregados/4709/periodos/2022/variaveis/93?localidades=N6[2604106]"
response = requests.get(link)
informacoes = response.json()

link2 = "https://servicodados.ibge.gov.br/api/v3/agregados/9514/periodos/2022/variaveis/93?localidades=N6[2604106]&classificacao=2[4,5]|287[100362]|286[113635]"
informacoesHM = requests.get(link2).json()

# Extraindo as informações necessárias Link2
populacao_homem = informacoesHM[0]['resultados'][0]['series'][0]['serie']['2022']
populacao_mulher = informacoesHM[0]['resultados'][1]['series'][0]['serie']['2022']

# Extraindo as informações necessárias Link1
id_cidade = informacoes[0]['resultados'][0]['series'][0]['localidade']['id']
nome_localidade = informacoes[0]['resultados'][0]['series'][0]['localidade']['nome']
populacao = informacoes[0]['resultados'][0]['series'][0]['serie']['2022']

fig_dados_city = go.Figure(data=[go.Table(
    header=dict(values=['ID Cidade', 'Localidade', 'População', 'População Homem', 'População Mulher'],
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[[id_cidade], [nome_localidade], [populacao],[populacao_homem], [populacao_mulher]],
               fill_color='lavender',
               align='left'))
])

# Informações da cidade


# Extraindo as informações necessárias







layout = dbc.Container([
    dbc.Row([
        dbc.Col([html.H1("Análise De Dados Por Cidade", className='text-Dash',  style={'textAlign': 'center'})], width=12),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id="choropleth-map", figure=fig), width=6),
        dbc.Col(dcc.Graph(figure=fig_dados_city), width=6)
    ])
])