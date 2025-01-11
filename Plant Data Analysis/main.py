import pandas as pd


df = pd.read_csv("iris.csv")

# Statistics
print(df.describe())

# Filtering by species
print(df[df['species']=='setosa'])

# Data Grouping
print(df.groupby('species')['sepal_length'].mean())