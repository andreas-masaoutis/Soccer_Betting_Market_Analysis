import plotly.graph_objects as go
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import dash_bootstrap_components as dbc


import plotly.express as px
import plotly.io as pio
import pandas as pd
import numpy as np


from app import app

# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

with open('dataset.md') as md_file:
    md_content = md_file.read()



## load the data
df1 = pd.read_pickle('main_bookmakers_1')
df2 = pd.read_pickle('main_bookmakers_2')
df3 = pd.read_pickle('main_bookmakers_3')

df = pd.concat([df1,df2,df3], axis=0)


bookmaker_name = ['B365', 'BS', 'BW', 'GB', 'IW', 'LB'
                  , 'PS', 'PSC', 'SB', 'SJ', 'VC', 'WH']
                  
bookmaker_selection = [bookie+'H' for bookie in bookmaker_name]



# change to app.layout if running as single page app instead
layout = html.Div( children = [
dcc.Markdown('''{}'''.format(md_content)),
dcc.Graph(id='graph-with-slider'),
    
    dcc.RadioItems( id='bookmaker-radio',
    
    ## watch out for the double comprehension, dictionary inside list
    options=[{ key:sign for key in ['label','value']} for sign in bookmaker_selection],
    value='B365H',
    labelStyle={'display': 'inline-block'}) ]
, style={"margin":"0% 10% ", "text-align":"center"}
)

# page callbacks
# choose between condensed table and full table


## the update mechanism for the page elements
@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('bookmaker-radio', 'value')])
def update_figure(bookie):
    summary_df = df.groupby(['Season', 'Div']).count()[[bookie, 'Date']]
    
    summary_df['rate'] = (summary_df[bookie] / summary_df['Date']) * 100
    
    summary_df = summary_df.reset_index()
    
    pivoted_df = pd.pivot_table(summary_df[['Season', 'Div','rate']],
                           values = "rate",
                           index = "Season",
                           columns = "Div"
                           )
                           
    fig = px.imshow( pivoted_df
    , labels=dict(color="Completion %")
    , template = 'plotly_dark'
               )

    return fig




# needed only if running this as a single page app
# if __name__ == '__main__':
#     app.run_server(host='127.0.0.1', debug=True)