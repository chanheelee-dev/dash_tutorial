import dash
from dash.dependencies import Input, Output, State
from dash import dcc, html, dash_table

import pandas as pd

# reference: 
# https://dash.plotly.com/dash-core-components/upload

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow ultiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-data-upload')
])
