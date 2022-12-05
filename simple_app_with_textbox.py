from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.H6("Change the value in the text box"),
    html.Div([
        "Input: ",
        dcc.Input(
            id="my-input",
            value="init value here",
            type="text"
        )
    ]),
    html.Br(),
    html.Div(id='my-output')
])

# @app.callback(
#     Output(component_id='my-output')
# )

if __name__ == "__main__":
    app.run_server(debug=True)
