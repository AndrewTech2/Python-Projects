import pandas

df = pandas.read_excel("Input.xlsx")

print(df.info())
print(df.head())
df['Total'] = df['Price'] * df['Quantity']

df.to_excel("output.xlsx")