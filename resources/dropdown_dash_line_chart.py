import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import flask
import pandas as pd
import time
import os

server = flask.Flask('app')
server.secret_key = os.environ.get('secret_key', 'secret')

df = pd.read_csv('/Users/winston/Desktop/foundations_final_project/data/gender_cases_per_year.csv', delimiter = ",", header=0)

app = dash.Dash('app', server=server)

app.scripts.config.serve_locally = False
dcc._js_dist[0]['external_url'] = 'https://cdn.plot.ly/plotly-basic-latest.min.js'

app.layout = html.Div([
    # html.H1('Human Trafficking Cases per Year by Gender'),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
        # replace value for corresponding key
            {'label': 'Female', 'value': 'Female'},
            {'label': 'Male', 'value': 'Male'},
            {'label': 'Unknown', 'value': 'Unknown'}
        ],
        value='UA'
    ),
    dcc.Graph(id='my-graph')
], className="container")

@app.callback(Output('my-graph', 'figure'),
              [Input('my-dropdown', 'value')])

def update_graph(selected_dropdown_value):
    dff = df[df['Gender'] == selected_dropdown_value]
    return {
        'data': [{
            'x': dff.year,
            'y': dff.cases,
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

if __name__ == '__main__':
    app.run_server()
