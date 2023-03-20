"""
This file holds the references to all the pages for this Dash app
"""
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

# must add this import in order for the app to be deployed successfully on Render
from my_app import server
from my_app import app

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
                        dbc.Col(html.Img(src="/assets/favicon.ico", height="40px")),
                        dbc.Col(
                            dbc.NavbarBrand(
                                "Soccer Betting Market Analysis", className="ml-2"
                            )
                        ),
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
                    [button_group],
                    className="ml-auto",
                    navbar=True,
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


def toggle_navbar_collapse(navbar_switch, is_open):
    """
    A on/off toggle for the navbar
    """
    if navbar_switch:
        return not is_open
    return is_open


for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

# embedding the navigation bar
app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        navbar,
        html.Div(id="page-content"),
        html.Footer(
            [
                dbc.Container(
                    [html.P("Soccer Betting Market Analysis - 2023")],
                    style={"text-align": "center", "font-size": "17px"},
                )
            ]
        ),
    ]
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    """
    The routes for the pages
    """
    if pathname == "/overround":
        return overround.layout
    if pathname == "/bias":
        return bias.layout
    if pathname == "/dataset":
        return dataset.layout
    if pathname == "/introduction":
        return introduction.layout
    if pathname == "/home":
        return home.layout


if __name__ == "__main__":
    app.run_server(debug=True)
