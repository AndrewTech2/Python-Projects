import pandas
import plotly_express as px

df = pandas.read_csv("employees.csv")
plot = px.scatter(df, x='PerformanceScore', y='Salary', color='Department')
plot.show()