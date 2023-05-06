"""
The analysis of the overround, along Divisions, Teams, and Seasons
"""
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import numpy as np
import dash_bootstrap_components as dbc

from my_app import app

# needed if running single page dash app instead
# external_stylesheets = [dbc.themes.LUX]

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


## load the data
df1 = pd.read_pickle("data/main_bookmakers_1")
df2 = pd.read_pickle("data/main_bookmakers_2")
df3 = pd.read_pickle("data/main_bookmakers_3")

df = pd.concat([df1, df2, df3], axis=0)

## In order to reduce the memory footprint we delete dfs we don't need anymore
del df1, df2, df3

bookmaker_name = [
    "B365",
    "BS",
    "BW",
    "GB",
    "IW",
    "LB",
    "PS",
    "PSC",
    "SB",
    "SJ",
    "VC",
    "WH",
]

columns_selection = [bookie + "_ovr" for bookie in bookmaker_name]

bookmaker_selection = [bookie + "_ovr" for bookie in bookmaker_name]


## The markdown file path is relative to index.py that imports this file
with open("apps/texts/overround.md", encoding="utf-8") as md_file:
    md_content = md_file.read()


## the main elements of the page
layout = html.Div(
    children=[
        dbc.Container(
            [
                dcc.Markdown(
                    f"""{md_content}""",
                    style={"text-align": "justify", "font-size": "17px"},
                ),
                html.P(
                    "The historical trend of the overround",
                    style={"text-align": "center", "font-size": "17px"},
                ),
                dcc.Graph(
                    figure=px.line(
                        df.groupby("Season")[columns_selection].mean(),
                        template="plotly_dark",
                        labels={"value": "Overround"},
                    )
                ),
                html.P(
                    "The overround per Team",
                    style={"text-align": "center", "font-size": "17px"},
                ),
                dcc.Graph(id="overround-year"),
                dcc.RadioItems(
                    id="year-radio",
                    ## watch out for the double comprehension, dictionary inside list
                    options=[
                        {key: year for key in ["label", "value"]}
                        for year in range(df["Season"].min(), 1 + df["Season"].max())
                    ],
                    value=2000,
                    labelStyle={"display": "inline-block"},
                ),
                html.P(
                    "The overround per Division",
                    style={"text-align": "center", "font-size": "17px"},
                ),
                dcc.Graph(id="overround-bookie"),
                dcc.RadioItems(
                    id="bookie-radio",
                    ## watch out for the double comprehension, dictionary inside list
                    options=[
                        {key: year for key in ["label", "value"]}
                        for year in bookmaker_selection
                    ],
                    value="B365_ovr",
                    labelStyle={"display": "inline-block"},
                ),
            ]
        )
    ]
)


## the update mechanism for the overround per team
@app.callback(Output("overround-year", "figure"), [Input("year-radio", "value")])
def update_figure_overround_per_team(selected_year):
    """The second chart"""
    filtered_df = (
        df[df["Season"] == selected_year]
        .groupby(["Div", "HomeTeam"])[columns_selection + ["Div"]]
        .mean()
        .droplevel(level=[0])
    )

    divs = df[df["Season"] == selected_year].groupby(["HomeTeam"])["Div"].last()

    filtered_df = filtered_df.join(divs)

    fig = px.line(
        filtered_df,
        template="plotly_dark",
        hover_data=["Div"],
        labels={"value": "Overround"},
    )

    fig.update_layout(transition_duration=500)

    return fig


## the update mechanism for the overround per division
@app.callback(Output("overround-bookie", "figure"), [Input("bookie-radio", "value")])
def update_figure_overround_per_division(bookie):
    """The last chart"""
    filtered_df = df[["HomeTeam", "Season", "Div"] + [bookie]]

    filtered_df = pd.pivot_table(
        filtered_df, values=bookie, index=["Div"], columns=["Season"], aggfunc=np.mean
    )

    fig = px.scatter(filtered_df, template="plotly_dark", labels={"value": "Overround"})

    fig.update_layout(transition_duration=500)

    return fig
