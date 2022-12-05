import dash
from dash import html
from dash import dcc

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Hello World!"),
    dcc.Tabs(
        id="tabs",
        children=[
            dcc.Tab(
                label="Tab 1",
                value="tab-1-value"
            ),
            dcc.Tab(
                label="Tab 2",
                value="tab-2-value"
            )
        ]
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
