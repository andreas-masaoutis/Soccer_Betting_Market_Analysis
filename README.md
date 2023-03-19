# Soccer_Betting_Market_Analysis

>An analytics dashboard on the relation between the favourite-longshot bias and the bookmaker's overround in soccer betting

This is the codebase for a Plotly-Dash [web app](https://soccer-betting-market-analysis.onrender.com/home), that displays data from the soccer betting market. The focus is on the hypothesis of the existence of the favourite-longshot bias. The hypothesis states that if you purely bet randomly, the expected return will be higher betting on favourites than betting on longshots - beware that in the case of random betting the expected return is still a loss equal to the bookmaker's overround.

### Structure
The code base is structured as a multi-page Dash app. The file **index.py** holds the routes to the individual pages, which are stored in the **apps** folder.

In order to separate the content, mostly text, and the actual page, all the text is stored in markdown files in the **texts** folder, which is then read by the individual apps/pages.

All the data are stored in three pickles in the **data** folder. We split them in order to reduce the size of the resulting files; other than that it is a simple dataframe with the betting data.

Various project documents, like the license and the requirements are in the **project_documents** folder.

The main ingredients used in this project are: 
- ![Python 3.8.6](https://img.shields.io/badge/python-3.8.6-blue.svg) Please note that different versions might fail when trying to read the pickled dataframes.
- ![Dash 1.17.0](https://img.shields.io/badge/dash-1.17.0-blue.svg)
