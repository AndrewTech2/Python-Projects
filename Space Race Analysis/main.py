import pandas, streamlit, plotly.express, datetime

months_index = {'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3, 'May': 4, 'Jun': 5, 'Jul': 6, 'Aug': 7, 'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11}

df = pandas.read_csv('mission_launches.csv')
prices_mean = sum(list(map(lambda x: float(x.replace(",", "")), df['Price'].dropna().to_dict().values()))) / len(list(map(lambda x: float(x.replace(",", '')), df['Price'].dropna().to_dict().values())))
df['Price'] = df['Price'].fillna(prices_mean)
year = []
months = []
for ind, row in df.iterrows():
    year.append(int(row['Date'].split()[3]))
    row['Price'] = float(str(row['Price']).replace(",", ''))
    date_values = row['Date'].split()
    month = months_index[date_values[1]]+1
    months.append(date_values[1])
    date = date_values[2].replace(",", '')
    try:
        date_time = datetime.datetime.strptime(f"{date_values[3]}-{month}-{date} {date_values[4]}", '%Y-%m-%d %H:%M')
    except:
        continue
    else:
        row['Date'] = date_time
        df.iloc[ind] = row
df['Year'] = year
df['Month'] = months
organisations  = []
for yr in set(year):
    df_per_year = df[df['Year'] == yr]
    org = df_per_year.groupby('Organisation').count()
    org = pandas.DataFrame(org)
    org = org.sort_values('Location', ascending=False)
    organisations.append(org.index[0])

streamlit.title("Space Race Data Visualization")
streamlit.write("1. Most missions launched by year, grouped by organisation")
streamlit.table({'Year': list(set(year)), 'Organisation': organisations})

streamlit.write("2. Cost variation of missions")
plot = plotly.express.line(df, x='Date', y='Price')
streamlit.plotly_chart(plot)

per_month = df.groupby("Month").count()
months = list(per_month.index)
expeditions = list(per_month['Organisation'])

streamlit.write("3. Popularity per month")
plot = plotly.express.bar({'Month': months, '# of expeditions': expeditions}, x='Month', y='# of expeditions')
streamlit.plotly_chart(plot)

percentages = []
for yr in set(year):
    df_per_year = df[df['Year'] == yr]
    success = df_per_year[df['Mission_Status'] == 'Success'].count()['Mission_Status']
    failure = df_per_year[df['Mission_Status'] == 'Failure'].count()['Mission_Status']
    suc_perc = 100 * success / (success + failure)
    percentages.append(suc_perc)

streamlit.write("4. Success Rate")
plot = plotly.express.line({'Year': list(set(year)), 'Rate': percentages}, x='Year', y='Rate')
streamlit.plotly_chart(plot)