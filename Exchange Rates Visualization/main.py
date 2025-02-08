import pandas, datetime, plotly.express as plt

df = pandas.read_csv("euro-daily-hist_1999_2022.csv")
df = df.rename(columns={'[US dollar ]': 'US_dollar', 'Period\\Unit:': 'Time'})
new_time = []
for x in df['Time']:
    new_time.append(datetime.datetime.strptime(x, '%Y-%m-%d'))
df['Time'] = new_time
df.sort_values('Time', inplace=True)
df = df.reset_index()
df = df.drop(columns=['index'])
for column in df.columns:
    if column not in ['Time', 'US_dollar']:
        df = df.drop(columns=[column])
euro_to_dollar = df
for ind, rate in df.iterrows():
    if '-' in str(rate['US_dollar']):
        df = df.drop(index=ind)
df['US_dollar'] = [float(rate) for rate in df['US_dollar']]
plot = plt.line(df, x='Time', y='US_dollar')
plot.show()