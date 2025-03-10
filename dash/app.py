# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import requests

# Function to fetch data from NocoDB
def get_nocodb_data():
    url = "https://automatic-yodel-9gxjg9x5997374g9-8000.app.github.dev/nocodb-data/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            records = data.get('records', [])
            print("Полученные данные:", records)
            cleaned_records = [
                {k: v for k, v in record.items() if not k.startswith('_nc_m2m_')}
                for record in records
            ]
            return pd.DataFrame(cleaned_records)
        else:
            print("Ошибка при получении данных:", response.status_code)
            return pd.DataFrame()
    except Exception as e:
        print(f"Ошибка соединения: {e}")
        return pd.DataFrame()

# Fetch data
df = get_nocodb_data()

# Initialize the app - incorporate a Dash Bootstrap theme
external_stylesheets = [dbc.themes.CERULEAN]
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
app.layout = dbc.Container([
    dbc.Row([
        html.Div('My First App with Data, Graph, and Controls', className="text-primary text-center fs-3")
    ]),

    dbc.Row([
        dbc.RadioItems(options=[{"label": x, "value": x} for x in df.columns if x in ['pop', 'lifeExp', 'gdpPercap']],
                       value='lifeExp',
                       inline=True,
                       id='radio-buttons-final')
    ]),

    dbc.Row([
        dbc.Col([
            dash_table.DataTable(data=df.to_dict('records'), page_size=12, style_table={'overflowX': 'auto'})
        ], width=6),

        dbc.Col([
            dcc.Graph(figure={}, id='my-first-graph-final')
        ], width=6),
    ]),

], fluid=True)

# Add controls to build the interaction
@callback(
    Output(component_id='my-first-graph-final', component_property='figure'),
    Input(component_id='radio-buttons-final', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)