from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
import assets
from app import app

# Leitura dos dados
df = pd.read_csv('Data/base_com_dados_geral.csv')
df_subgrupos = pd.read_csv('Data/subgrupos_geral.csv')

# Definição do layout
layout = dbc.Container([
    dbc.Row([
        html.Div([
            dbc.ButtonGroup([
                dbc.Button("Geral", id="btn-geral", className="botoes-tela-principal-inicio line-bottom"),
                dbc.Button("Rural", id="btn-rural", className="line-bottom"),
                dbc.Button("Quilombola", id="btn-quilombola", className="line-bottom"),
                dbc.Button("Analfabetas", id="btn-analfabetas", className="line-bottom"),
                dbc.Button("Menor que 15", id="btn-menor-15", className="line-bottom"),
                dbc.Button("Cidade com +10k", id="btn-cidade-10k", className="line-bottom"),
                dbc.Button("BF", id="btn-bf", className="botoes-tela-principal-fim")
            ],size="lg",),
        ],
        )], style={'margin-bottom': '10px'}, className='botoes'),

    dbc.Row([
        dbc.Col([
            html.H1(id='titulo_pagina', className='text-Dash'),
        ]),
    ]),

    dbc.Row([
        dbc.Col([
            html.Div([
                dcc.Graph(id='figura_Dp_Dn')
            ], className='Geral'),
        ], width=6, className='Geral'),
    ], className='Geral'),

], fluid=True)


# Callback para atualizar o título da página e o gráfico com base na base selecionada
@app.callback(
    [Output('titulo_pagina', 'children'),
     Output('figura_Dp_Dn', 'figure')],
    [Input('btn-geral', 'n_clicks'),
     Input('btn-rural', 'n_clicks'),
     Input('btn-quilombola', 'n_clicks'),
     Input('btn-analfabetas', 'n_clicks'),
     Input('btn-menor-15', 'n_clicks'),
     Input('btn-cidade-10k', 'n_clicks'),
     Input('btn-bf', 'n_clicks')]
)
def update_figure_and_title(geral_clicks, rural_clicks, quilombola_clicks, analfabetas_clicks, menor_15_clicks, cidade_10k_clicks, bf_clicks):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = 'btn-geral'  # Seleciona "Geral" por padrão
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # Filtra os dados com base na base selecionada
    if button_id == 'btn-geral':
        df_filtrado = df[df['Base'] == 'all']
        titulo = "Análise de Dados - Geral"
    elif button_id == 'btn-rural':
        df_filtrado = df[df['Base'] == 'rural']
        titulo = "Análise de Dados - Rural"
    elif button_id == 'btn-quilombola':
        df_filtrado = df[df['Base'] == 'quilombola']
        titulo = "Análise de Dados - Quilombola"
    elif button_id == 'btn-analfabetas':
        df_filtrado = df[df['Base'] == 'analfabetas']
        titulo = "Análise de Dados - Analfabetas"
    elif button_id == 'btn-menor-15':
        df_filtrado = df[df['Base'] == 'menor 15']
        titulo = "Análise de Dados - Menor que 15 anos"
    elif button_id == 'btn-cidade-10k':
        df_filtrado = df[df['Base'] == '10k']
        titulo = "Análise de Dados - Cidade com 10 mil habitantes ou mais"
    elif button_id == 'btn-bf':
        df_filtrado = df[df['Base'] == 'BF']
        titulo = "Análise de Dados - BF"

    # Atualiza os gráficos com os dados filtrados
    figura_Dp_Dn = go.Figure(
        data=[
            go.Bar(
                x=['Com baixo peso', 'Sem baixo peso'],
                y=[df_filtrado['Dp'].iloc[0], df_filtrado['Dn'].iloc[0]],
                text=[f'{df_filtrado["Dp"].iloc[0]} {df_filtrado["DpPorcento"].iloc[0][:4]}%', f'{df_filtrado["Dn"].iloc[0]}  {df_filtrado["DnPorcento"].iloc[0][:4]}%'],
                textposition='auto',
                marker=dict(
                    color=['#7D8AFF', '#4252DD']
                )
            )
        ]
    )
    figura_Dp_Dn.update_layout(title_text='Total de exemplos')
    figura_Dp_Dn.update_yaxes(title_text='Número de crianças')
    figura_Dp_Dn.update_xaxes(tickvals=[0, 1], ticktext=['Com baixo peso', 'Sem baixo peso'])

    # Retorno dos gráficos atualizados e do título da página
    return titulo, figura_Dp_Dn
