import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as dhtml
import plotly
import plotly.graph_objs as plgo

import random

from collections import deque

X = deque(maxlen=20)
Y = deque(maxlen=20)

X.append(1)
Y.append(1)

app = dash.Dash(__name__)

app.layout = dhtml.Div(
    [
        dcc.Graph(id='testGraph', animate=True),
        dcc.Interval(id='updateInterval', interval=5*1000, n_intervals=0)
    ]
)


@app.callback(Output('testGraph', 'figure'),
              [Input('updateInterval', 'n_intervals')])
def update_something(n):
    X.append(X[-1] + 1)
    Y.append(Y[-1] + Y[-1] * random.uniform(-0.1, 0.1))

    data = plotly.graph_objs.Scatter(
        x=list(X),
        y=list(Y),
        name='Scatter',
        mode='lines+markers'
    )

    return {'data': [data], 'layout': plgo.Layout(xaxis=dict(range=[min(X), max(X)]),
                                                  yaxis=dict(range=[min(Y), max(Y)]))}


if __name__ == '__main__':
    app.run_server(debug=True)
