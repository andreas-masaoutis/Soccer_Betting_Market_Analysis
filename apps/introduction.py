import plotly.graph_objects as go
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import dash_bootstrap_components as dbc

from my_app import app

# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

with open('introduction.md') as md_file:
    md_content = md_file.read()


# change to app.layout if running as single page app instead
layout = html.Div( children = [
dcc.Markdown('''{}'''.format(md_content))]
, style={"margin":"0% 10% ", "text-align":"justify"}
)

# page callbacks
# choose between condensed table and full table





# needed only if running this as a single page app
# if __name__ == '__main__':
#     app.run_server(host='127.0.0.1', debug=True)
