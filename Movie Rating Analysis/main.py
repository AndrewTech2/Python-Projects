import pandas, plotly_express as plt

df = pandas.read_csv("movies.csv")
df = df.groupby("Rating").count()
df.columns = ['Number of Ratings', 'temporary', 'temporary']
print(df)
plot = plt.bar(df, x=df.index, y='Number of Ratings')
plot.show()