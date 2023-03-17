import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

# must add this line in order for the app to be deployed successfully on Heroku
from app import server
from app import app
# import all pages in the app
from apps import overround, bias, home, dataset, introduction

# building the navigation bar
# https://github.com/facultyai/dash-bootstrap-components/blob/master/examples/advanced-component-usage/Navbars.py



button_group = dbc.ButtonGroup(
    children=[
        dbc.Button("Home", href="/home"),
        dbc.Button("Introduction", href="/introduction"),
        dbc.Button("The dataset", href="/dataset"),
        dbc.Button("Overround", href="/overround"),
        dbc.Button("Longshot bias", href="/bias"),
    ],

)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="/assets/ball.png", height="40px")),
                        dbc.Col(dbc.NavbarBrand("Soccer Betting Market Analysis", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/home",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    # right align dropdown menu with ml-auto className
                    [button_group], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-4",
)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

# embedding the navigation bar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/overround':
        return overround.layout
    elif pathname == '/bias':
        return bias.layout
    elif pathname == '/dataset':
        return dataset.layout
    elif pathname == '/introduction':
        return introduction.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=True)
