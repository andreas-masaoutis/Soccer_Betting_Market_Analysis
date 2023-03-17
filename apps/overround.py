import plotly.graph_objects as go
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.io as pio
import pandas as pd
import numpy as np

from app import app

# needed if running single page dash app instead
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


## load the data
df1 = pd.read_pickle('main_bookmakers_1')
df2 = pd.read_pickle('main_bookmakers_2')
df3 = pd.read_pickle('main_bookmakers_3')

df = pd.concat([df1,df2,df3], axis=0)


bookmaker_name = ['B365', 'BS', 'BW', 'GB', 'IW', 'LB'
                  , 'PS', 'PSC', 'SB', 'SJ', 'VC', 'WH']
                  
columns_selection = [bookie+'_ovr' for bookie in bookmaker_name]

bookmaker_selection = [bookie+'_ovr' for bookie in bookmaker_name]


with open('overround.md') as md_file:
    md_content = md_file.read()



## the main elements of the page
layout = html.Div(children=[
    dcc.Markdown('''{}'''.format(md_content) ,style={"margin":"0% 10% ", "text-align":"justify"} ) ,
    
    dcc.Graph(figure = px.line(df.groupby('Season')[columns_selection].mean(),template = 'plotly_dark')),

    dcc.Graph(id='overround-year'),
    
    dcc.RadioItems( id='year-radio',
    
    ## watch out for the double comprehension, dictionary inside list
    options=[{ key:year for key in ['label','value']} for year in range(df['Season'].min(),1+df['Season'].max()
    )],
    value=2000,
    labelStyle={'display': 'inline-block'})
    
    ,dcc.Graph(id='overround-bookie'),
    
    dcc.RadioItems( id='bookie-radio',
    
    ## watch out for the double comprehension, dictionary inside list
    options=[{ key:year for key in ['label','value']} for year in bookmaker_selection],
    value='B365_ovr',
    labelStyle={'display': 'inline-block'}) 
    
])



## the update mechanism for the page elements
@app.callback(
    Output('overround-year', 'figure'),
    [Input('year-radio', 'value')])
def update_figure(selected_year):

    filtered_df = df[df['Season'] == selected_year].groupby([
        'Div', 'HomeTeam'])[columns_selection + ['Div']].mean().droplevel(
    level=(0)) 
    
    divs = df[df['Season'] == selected_year].groupby([
         'HomeTeam'])['Div' ].last()
         
    filtered_df = filtered_df.join(divs)

    fig = px.line(filtered_df

        , template = 'plotly_dark'
        , hover_data= ['Div']
        )

    fig.update_layout(transition_duration=500)

    return fig


## the update mechanism for the page elements
@app.callback(
    Output('overround-bookie', 'figure'),
    [Input('bookie-radio', 'value')])
def update_figure(bookie):
    filtered_df = df[['HomeTeam', 'Season', 'Div'] + [bookie]]

    filtered_df =  pd.pivot_table(filtered_df, values=bookie, index=['Div'],
                    columns=['Season'], aggfunc=np.mean)
    

    fig = px.scatter(filtered_df

        ,template = 'plotly_dark')

    fig.update_layout(transition_duration=500)

    return fig


# needed only if running this as a single page app
# if __name__ == '__main__':
#     app.run_server(host='127.0.0.1', debug=True)
