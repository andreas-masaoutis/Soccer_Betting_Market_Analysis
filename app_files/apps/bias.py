"""
The page with the favourite-longshot bias 
"""
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import dash_bootstrap_components as dbc


from my_app import app

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

columns_list = [
    [name + suffix for suffix in ["H", "D", "A", "_ovr"]] for name in bookmaker_name
]
signs = ["H", "D", "A"]


options = (
    [{"label": avalue, "value": akey} for akey, avalue in enumerate(bookmaker_name)],
)

## The markdown file path is relative to index.py that imports this file
with open("apps/texts/bias.md", encoding="utf-8") as md_file:
    md_content = md_file.read()


# change to app.layout if running as single page app instead
layout = layout = html.Div(
    children=[
        dbc.Container(
            [
                dcc.Markdown(
                    f"""{md_content}""",
                    style={"text-align": "justify", "font-size": "17px"},
                ),
                dcc.Graph(id="graph-bias"),
                dcc.RadioItems(
                    id="bookie-radio",
                    ## watch out for the double comprehension, dictionary inside list
                    options=[
                        {"label": avalue, "value": akey}
                        for akey, avalue in enumerate(bookmaker_name)
                    ],
                    value=0,
                    labelStyle={"display": "inline-block"},
                ),
                dcc.RangeSlider(
                    id="year--range-slider",
                    min=df["Season"].min(),
                    max=df["Season"].max(),
                    value=[df["Season"].min(), df["Season"].max()],
                    marks={str(year): str(year) for year in df["Season"].unique()},
                    step=1,
                ),
            ]
        )
    ]
)

# page callbacks
# choose between condensed table and full table


@app.callback(Output("year--range-slider", "value"), [Input("bookie-radio", "value")])
def set_years_options(selected_bookie):
    """
    Find the years for which a specific bookmaker has quoted prices for match outcomes
    """
    specific_years = list(
        df[df[(bookmaker_name[selected_bookie] + "H")].notnull()]["Season"].unique()
    )

    print(selected_bookie)
    return [min(specific_years), max(specific_years)]


@app.callback(
    [
        Output("year--range-slider", "marks"),
        Output("year--range-slider", "min"),
        Output("year--range-slider", "max"),
    ],
    [Input("year--range-slider", "value")],
)
def set_year_value(available_options):
    """
    The range of year values for which a specific bookmaker has quoted prices for match outcomes
    """
    return (
        {str(year): str(year) for year in available_options},
        min(available_options),
        max(available_options),
    )


@app.callback(
    Output("graph-bias", "figure"),
    [
        Input("bookie-radio", "value"),
        Input("year--range-slider", "value"),
        # Input("year--range-slider", "min"),
        # Input("year--range-slider", "max"),
    ],
)
def update_figure(bookie, year):
    """
    Simple figure update
    """

    seasons_df = df[(df["Season"] >= year[0]) & (df["Season"] <= year[1])]

    print(f"You have selected {year}")

    fig = make_subplots(rows=1, cols=3, shared_yaxes=True)

    for i in range(3):
        bookie_selection_df = (
            seasons_df[columns_list[bookie] + ["FTR"]]
            .dropna()
            .sort_values(by=columns_list[bookie][i])
        )

        bookie_selection_df["bins"] = pd.qcut(
            bookie_selection_df[f"{columns_list[bookie][i]}"],
            q=50,
            duplicates="drop",
        )

        bookie_selection_df["success"] = bookie_selection_df.FTR.apply(
            lambda x: 1 if x == f"{signs[i]}" else 0
        )

        grouped_df = bookie_selection_df.groupby("bins").mean()

        grouped_df["return_rate"] = bookie_selection_df.groupby("bins").apply(
            lambda x: (np.mean((x["success"]) * (x[f"{columns_list[bookie][i]}"])))
        )

        fig.add_trace(
            go.Scatter(
                x=list(range(len(list(grouped_df.return_rate)))),
                y=list(grouped_df.return_rate),
                mode="lines",
                name="Return_" + signs[i],
            ),
            row=1,
            col=i + 1,
        )

        fig.add_trace(
            go.Scatter(
                x=list(range(len(list(grouped_df.return_rate)))),
                y=2 - grouped_df[f"{columns_list[bookie][3]}"],
                name="1-Overround_" + signs[i],
            ),
            row=1,
            col=i + 1,
        )

    fig.update_layout(title_text="Multiple Subplots for HomeWin, Draw, and AwayWin")
    fig.update_layout(yaxis={"range": [0.7, 1.1]}, template="plotly_dark")

    return fig
