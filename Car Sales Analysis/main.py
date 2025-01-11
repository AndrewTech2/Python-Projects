import pandas as pd

df = pd.read_csv('sales.csv')
for column_name in df.columns:
    try:
        df[column_name] = df[column_name].fillna(df[column_name].mean())
    except TypeError:
        continue
df['sales_diff'] = abs(df['sales'] - df['sales'].mean())
month_list = []
for element in df['order_date']:
    month_list.append(str(element).split("-")[1])
month = pd.Series(month_list)
df['month'] = month
df2 = df.groupby('month')['sales'].mean()
print(df2)