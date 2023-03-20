"""
The home/main page
"""
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc


# needed only if running this as a single page app
# external_stylesheets = [dbc.themes.LUX]

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

with open("texts/home.md", encoding="utf-8") as md_file:
    md_content = md_file.read()


# change to app.layout if running as single page app instead
layout = html.Div(
    [
        dbc.Container(
            [
                html.Div(
                    [dcc.Markdown(f"""{md_content}""")],
                    style={"text-align": "justify", "font-size": "17px"},
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                children=[
                                    html.H3(
                                        children="Get the original datasets used for these dashboards",
                                        className="text-center",
                                    ),
                                    dbc.Button(
                                        "Data files",
                                        href="https://www.football-data.co.uk/downloadm.php",
                                        color="primary",
                                        className="mt-3",
                                    ),
                                ],
                                body=True,
                                color="dark",
                                outline=True,
                            ),
                            width=6,
                            className="mb-4",
                        ),
                        dbc.Col(
                            dbc.Card(
                                children=[
                                    html.H3(
                                        children="Access the code used to build these dashboards",
                                        className="text-center",
                                    ),
                                    dbc.Button(
                                        "GitHub",
                                        href="https://github.com/andreas-masaoutis/Soccer_Betting_Market_Analysis",
                                        color="primary",
                                        className="mt-3",
                                    ),
                                ],
                                body=True,
                                color="dark",
                                outline=True,
                            ),
                            width=6,
                            className="mb-4",
                        ),
                    ],
                    className="mb-5",
                ),
            ]
        )
    ]
)
