
from dash import Dash, html, dcc,Input, Output, callback
import plotly.express as px
import pandas as pd

external_stylesheets = ['style.css']

# Building the dash application
app = Dash(__name__, external_stylesheets=external_stylesheets)

# Reading the data into dataframe
df = pd.read_csv('merged_sales_data.csv')

# Plotting line graph for sales data with date
fig = px.line(df, x='date',
              y='Sales',
              labels={'date':'Dates','Sales':"Sales ($)"})


app.layout = html.Div(children=[
    html.H1(children='Soul Foods - Pink Morsel Sales Analysis'),
    # Radio Button
    dcc.RadioItems(['North', 'East ','South','West','All'], 'All', inline=True,id='region-radio-items'),

    html.Br(),

    html.Div(id='line_fig_title'),
    dcc.Graph(
        id='sales_graph',
        figure=fig
    )
])


@callback(
    Output('sales_graph', 'figure'),
    Output('line_fig_title','children'),
    Input('region-radio-items', 'value')
)
def update_layout(selected_radio_item):
    if selected_radio_item == 'All':
        title = "Pink Morsel Sales - {} Regions".format(selected_radio_item)
        fig = px.line(df, x='date',
                      y='Sales',
                      labels={'date': 'Dates', 'Sales': "Sales ($)"})
        return fig,title
    else:
        dff = df[df['region'] == selected_radio_item.lower()]
        title = "Pink Morsel Sales - {} Region".format(selected_radio_item)
        fig = px.line(dff, x='date',
                      y='Sales',
                      labels={'date': 'Dates', 'Sales': "Sales ($)"})
        return fig,title


# Add the external CSS file
app.css.append_css({'external_url': 'style.css'})

if __name__ == '__main__':
    app.run(debug=True)
