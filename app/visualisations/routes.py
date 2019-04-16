from flask import (
    Blueprint, Flask, flash, g, redirect, render_template, request, url_for, current_app
)

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import flask
import pandas as pd
import time
import os

viz = Blueprint('visualisations', __name__)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/hello-world-stock.csv')

# app = dash.Dash('app', server=server)

# app.scripts.config.serve_locally = False
# dcc._js_dist[0]['external_url'] = 'https://cdn.plot.ly/plotly-basic-latest.min.js'

# app.layout = html.Div([
#     html.H1('Stock Tickers'),
#     dcc.Dropdown(
#         id='my-dropdown',
#         options=[
#             {'label': 'Tesla', 'value': 'TSLA'},
#             {'label': 'Apple', 'value': 'AAPL'},
#             {'label': 'Coke', 'value': 'COKE'}
#         ],
#         value='TSLA'
#     ),
#     dcc.Graph(id='my-graph')
# ], className="container")

@viz.callback(Output('my-graph', 'figure'),
              [Input('my-dropdown', 'value')])

def update_graph(selected_dropdown_value):
    dff = df[df['Stock'] == selected_dropdown_value]
    return {
        'data': [{
            'x': dff.Date,
            'y': dff.Close,
            'line': {
                'width': 3,
                'shape': 'spline'
            }
        }],
        'layout': {
            'margin': {
                'l': 30,
                'r': 20,
                'b': 30,
                't': 20
            }
        }
    }