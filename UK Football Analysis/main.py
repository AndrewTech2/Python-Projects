import pandas, plotly_express
from pandas import DataFrame, Index

teams = {}
df = pandas.read_csv('E0.csv')
matches = df.to_dict(orient='records')

for match in matches:
    if match['HomeTeam'] not in teams.keys():
        teams[match['HomeTeam']] = 0
    if match['AwayTeam'] not in teams.keys():
        teams[match['AwayTeam']] = 0
    teams[match['HomeTeam']] += match['FTHG']
    teams[match['AwayTeam']] += match['FTAG']

teams = DataFrame({'Teams': teams.keys(), 'Total Goals': teams.values()})

plot = plotly_express.bar(teams, x='Teams', y='Total Goals')
plot.show()