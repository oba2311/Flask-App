# from: https://dash.plotly.com/getting-started

# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
# heatmap with plotly from:
# https://plotly.com/python/heatmaps/
import plotly.graph_objects as go
import datetime
import numpy as np
np.random.seed(1)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)



# # get data
#
# # from:
# # https://colab.research.google.com/drive/1x5Y6rdI-diB7YrW9349zh5g1-Q2wNfVd?usp=sharing
#
# # Retrieve data files
# import requests
# from datetime import datetime
#
# normal_data_url = 'http://coronadata.webiks.com/data.json'
# r = requests.get(normal_data_url)
# normal_data = r.json()
#
# folded_data_url = 'http://coronadata.webiks.com/folded_data.json'
# r = requests.get(folded_data_url)
# folded_data = r.json()
#
# updateTime = datetime.fromtimestamp(normal_data['lastUpdateDate'] / 1000)
# print(f'latst update date: {updateTime.isoformat()}')
#
# # Convert nodes to panda's dataframe
# import pandas as pd
#
#
# def split_coordinates(node):
#     coordinates = node['coordinates'].split(',')
#     try:
#         node['lat'] = float(coordinates[0].strip())
#     except ValueError as e:
#         pass
#     try:
#         node['lon'] = float(coordinates[1].strip())
#     except:
#         pass
#
#     return node
#
#
# nodes_with_coordinates = [split_coordinates(x) for i, x in enumerate(normal_data['data']['nodes']) \
#                           if 'coordinates' in normal_data['data']['nodes'][i] \
#                           and normal_data['data']['nodes'][i]['coordinates']]
#
# df = pd.DataFrame.from_dict(nodes_with_coordinates)
# # df.head()
#
#
# df.to_csv(r"C:/Users/omer/Desktop/Omer/Corona/data/nodes_data.csv", index=False)