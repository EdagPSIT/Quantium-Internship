
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


# Building the dash application
app = Dash(__name__)

# Reading the data into dataframe
df = pd.read_csv('merged_sales_data.csv')

# Plotting line graph for sales data with date
fig = px.line(df, x='date',
              y='Sales',
              labels={'date':'Dates','Sales':"Sales ($)"})


app.layout = html.Div(children=[
    html.H1(children='Soul Foods - Pink Morsel Sales Analysis'),

    html.Div(children='''
        Pink Morsel Sales trend
    '''),

    dcc.Graph(
        id='sales_graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
