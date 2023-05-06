# Soccer_Betting_Market_Analysis

>An analytics dashboard on the relation between the favourite-longshot bias and the bookmaker's overround in soccer betting

This is the codebase for a Plotly-Dash [web app](https://soccer-betting-market-analysis.onrender.com/home), that displays data from the soccer betting market. The focus is on the hypothesis of the existence of the favourite-longshot bias. The hypothesis states that if you purely bet randomly, the expected return will be higher betting on favourites than betting on longshots - beware that in the case of random betting the expected return is still a loss equal to the bookmaker's overround.

### Structure
The code for the app is located in the app_files folder, and it is structured as a multi-page Dash app. The file **app_files/index.py** holds the routes to the individual pages, which are stored in the **app_files/apps** folder.

In order to separate the content, mostly text, and the actual page, all the text is stored in markdown files in the **app_files/apps/texts** folder, which is then read by the individual apps/pages.

All the data are stored in three pickles in the **app_files/data** folder. We split them in order to reduce the size of the resulting files; other than that it is a simple dataframe with the betting data. 

Various project documents, like the license and the requirements are in the **project_documents** folder.

At the root level you will find docker files for building a container for the app.

### How to use
Clone the repository and then either:

- Create and activate a venv and then run **python index.py** from a terminal or **index.py** from an IDE
- Build the image using the Dockerfile and then run it mapping ports at 8050:8050
- Use docker-compose and execute the yaml file

In all these cases, the app should be accessible at http://localhost:8050/home, or http://0.0.0.0:8050/home 

* * *

This project uses: 
- ![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)
- ![Dash 1.17.0](https://img.shields.io/badge/dash-1.17.0-blue.svg)
