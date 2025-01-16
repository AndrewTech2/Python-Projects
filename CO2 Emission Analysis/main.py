import plotly_express as plt
import pandas, datetime

df = pandas.read_csv('co2.csv')
dates = []
for x in df.iterrows():
    dates.append(datetime.datetime(year=int(x[1]['Year']), month=int(x[1]['Month']), day=1))
dates = pandas.Series(dates)
df['Dates'] = dates
plot = plt.line(data_frame={'CO2 Level': df['CO2_Level'], 'Dates': df['Dates']}, x='Dates', y='CO2 Level')
plot.show()