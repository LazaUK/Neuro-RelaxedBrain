# Last update on 18/10/2021
# Last update by Laziz

import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import flask
import plotly
import plotly.graph_objs as go
from collections import deque

X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server,external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True

app.layout = html.Div(children=[
    html.H1(children='Laziz T. - My DEMO of Brain-Computer Interface'),
    html.Div(children='''
        I'll visualise here EEG telemetry
    '''),

    dcc.Graph(id='live-graph', animate=True),
    
    dcc.Interval(
        id='graph-update',
        interval=1*1000,
        n_intervals=0
    ),
])

@app.callback(Output('live-graph', 'figure'),
[Input('graph-update', 'n_intervals')])

def update_graph_scatter(n):
    X, Y # here I'm going to serve EEG data

    data = plotly.graph_objs.Scatter(
        x=list(X),
        y=list(Y),
        name='Scatter',
        mode= 'lines+markers'
    )

    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]), yaxis=dict(range=[min(Y),max(Y)]),)}

if __name__ == '__main__':
    app.run_server(debug=True)