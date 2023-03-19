"""
The introductory page
"""
import dash_core_components as dcc
import dash_html_components as html

with open("texts/introduction.md", encoding="utf-8") as md_file:
    md_content = md_file.read()


# change to app.layout if running as single page app instead
layout = html.Div(
    children=[dcc.Markdown(f"""{md_content}""")],
    style={"margin": "0% 10% ", "text-align": "justify"},
)
