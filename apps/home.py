"""
The home/main page
"""
import dash_html_components as html
import dash_bootstrap_components as dbc

# needed only if running this as a single page app
# external_stylesheets = [dbc.themes.LUX]

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change to app.layout if running as single page app instead
layout = html.Div(
    [
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            html.H1(
                                "The relation between the favourite - longshot bias\
            and the bookmaker's overround",
                                className="text-center",
                            ),
                            className="mb-5 mt-5",
                        )
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            html.H5(
                                children="The favourite - longshot bias is well \
            studied in the economics literature that analyses that beting market."
                            ),
                            className="mb-4",
                        )
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            html.H5(
                                children="The first page gives an overview of the literature. \
            The second presents the dataset we will use. The third and fourth pages analyse \
            the favourite - longshot bias and the overround respectively, by season, bookmaker \
            and division. Finally we see how the overround affects the bias"
                            ),
                            className="mb-5",
                        )
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                children=[
                                    html.H3(
                                        children="Get the original datasets used in this dashboard",
                                        className="text-center",
                                    ),
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                dbc.Button(
                                                    "CSV files",
                                                    href="https://www.football-data.co.uk/downloadm.php",
                                                    color="primary",
                                                ),
                                                className="mt-3",
                                            ),
                                            dbc.Col(
                                                dbc.Button(
                                                    "Database",
                                                    href="https://andreas-masaoutis.github.io",
                                                    color="primary",
                                                ),
                                                className="mt-3",
                                            ),
                                        ],
                                        justify="center",
                                    ),
                                ],
                                body=True,
                                color="dark",
                                outline=True,
                            ),
                            width=4,
                            className="mb-4",
                        ),
                        dbc.Col(
                            dbc.Card(
                                children=[
                                    html.H3(
                                        children="Access the code used to build this dashboard",
                                        className="text-center",
                                    ),
                                    dbc.Button(
                                        "GitHub",
                                        href="https://github.com/andreas-masaoutis",
                                        color="primary",
                                        className="mt-3",
                                    ),
                                ],
                                body=True,
                                color="dark",
                                outline=True,
                            ),
                            width=4,
                            className="mb-4",
                        ),
                        dbc.Col(
                            dbc.Card(
                                children=[
                                    html.H3(
                                        children="Read the blog article detailing the process",
                                        className="text-center",
                                    ),
                                    dbc.Button(
                                        "My Blog",
                                        href="https://andreas-masaoutis.github.io",
                                        color="primary",
                                        className="mt-3",
                                    ),
                                ],
                                body=True,
                                color="dark",
                                outline=True,
                            ),
                            width=4,
                            className="mb-4",
                        ),
                    ],
                    className="mb-5",
                ),
            ]
        )
    ]
)
