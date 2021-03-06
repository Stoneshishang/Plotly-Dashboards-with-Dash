import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../data/mpg.csv')

app = dash.Dash()
# ['mpg', 'hp', 'displacement'...]
features = df.columns

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(id='xaxis',
                     options=[{'label': i, 'value': i}
                              for i in features],  # python list comprehension
                     value='displacement')
    ], style={'width': '48%', 'display': 'inline-block'}),
    html.Div([
        dcc.Dropdown(id='yaxis',
                     options=[{'label': i, 'value': i}
                              for i in features],  # i is the column name
                     value='mpg'
                     )
    ], style={'width': '48%', 'display': 'inline-block'}),
    dcc.Graph(id='feature-graphic')
], style={'padding': 10})


@app.callback(Output('feature-graphic', 'figure'),  # the figure inserted into the line 26 Graph.
              [Input('xaxis', 'value'),     # the xaxis connected to the parameter that pass in below function at line 33.
               Input('yaxis', 'value')])
def update_graph(xaxis_name, yaxis_name):
    return {'data': [go.Scatter(x=df[xaxis_name],
                                y=df[yaxis_name],
                                text=df['name'],
                                mode='markers',  # make sure it is a scatter plot, not a line plot
                                marker={'size': 15})],
            'layout': go.Layout(title='My Dashboard for MPG',
                                xaxis={'title': xaxis_name},
                                yaxis={'title': yaxis_name})}


if __name__ == '__main__':
    app.run_server()
