## An introdcution and description of the dataset

Our dataset is available at [football-data.co.uk](https://www.football-data.co.uk/downloadm.php "The download page for the data"). It consists of a series of CSV or XLSX files where each row corresponds to a soccer match from a selection of European leagues


#### The leagues
Take a look at the leagues for which data is available.

| Division | Country     | League Name       |
|----------|-------------|-------------------|
| B1       | Belgium     | Jupiler League    |
| D1       | Germany     | Bundesliga 1      |
| D2       | Germany     | Bundesliga 2      |
| E0       | England     | Premiership       |
| E1       | England     | Division 1        |
| E2       | England     | Division 2        |
| E3       | England     | Division 3        |
| F1       | France      | Le Championat     |
| F2       | France      | Division 2        |
| G1       | Greece      | Ethniki Katigoria |
| I1       | Italy       | Serie A           |
| I2       | Italy       | Serie B           |
| N1       | Netherlands | KN Eredivisie     |
| P1       | Portugal    | Liga I            |
| SC0      | Scotland    | Division 1        |
| SC1      | Scotland    | Division 1        |
| SP1      | Spain       | La Liga Premera   |
| SP2      | Spain       | La Liga Segunda   |
| T1       | Turkey      | Ligi 1            |

 
#### The bookmakers
These are the bookmakers for which data is available.


| Bookmaker sign | Bookmaker name |
|----------------|----------------|
| B365           | Bet365         |
| BS             | Blue Square    |
| BW             | Bet&Win        |
| GB             | Gamebookers    |
| IW             | Interwetten    |
| LB             | Ladbrokes      |
| PS             | Pinnacle       |
| PSC            | Pinnacle closing|
| SB             | Sportingbet    |
| SJ             | Stan James     |
| VC             | VC Bet         |
| WH             | William Hill   |

 

#### The dataset
This is a small snapshot of the data.


| Div | Date       | HomeTeam | AwayTeam | FTHG | FTAG | FTR | B365H | B365D | B365A |
|-----|------------|----------|----------|------|------|-----|-------|-------|-------|
| I1  | 18/08/2018 | Chievo   | Juventus | 2    | 3    | A   | 13    | 5.75  | 1.25  |
| I1  | 18/08/2018 | Lazio    | Napoli   | 1    | 2    | A   | 2.8   | 3.4   | 2.5   |
| I1  | 19/08/2018 | Bologna  | Spal     | 0    | 1    | A   | 2.25  | 3.2   | 3.4   |
| I1  | 19/08/2018 | Empoli   | Cagliari | 2    | 0    | H   | 2.14  | 3.2   | 3.6   |
| I1  | 19/08/2018 | Parma    | Udinese  | 2    | 2    | D   | 2.45  | 3.3   | 2.9   |

 
This is the core of the data that we will use:

- the specifics of the match, like date, division, teams, and result
- and the market data, the quoted prices for 1-X-2 by the various bookmakers 

Please note that the original dataset for some leagues contains more data:

- for the matches, like shots on target, red cards, etc, 
- for the market, under/over prices, asian handicap, etc.

while at the same time we will compute our own, such as the overround.

We will concern ourselves with the core, since these are the data most relevant for calculating the overround, but also because the rest of the data is not always available. For more pieces on information take a look at the notes section of the [source page](https://www.football-data.co.uk/notes.txt "The notes section on the data by football-data.co.uk")

In order to collect all the data, calculate the overround along other relevant features, and finally filter out what we want, we have created a database using MongoDB. For the details and the relevant code of this process, take a look at the [blog page](https://andreas-masaoutis.github.io "My blog") that describe the process.


#### The available data

The following figure provides a compact view of the availability of data. We start with the 2000 soccer season, all the way to 2018. Not all bookmakers were operating during all seasons, and sometimes they would not quote prices for all matches of a league.

 
 
 

