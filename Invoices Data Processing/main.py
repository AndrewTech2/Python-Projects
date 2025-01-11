import pandas, os
import pandas as pd
from pandas import DataFrame

dataframes = {}
for file in os.listdir('invoices'):
    dataframes[f'df{os.listdir('invoices').index(file)+1}'] = pandas.read_csv(os.path.join('invoices', file))
df1, df2, df3 = dataframes['df1'], dataframes['df2'], dataframes['df3']
master_df = pandas.concat([df1, df2, df3])
print(master_df)
print(f"Number of invoices: {len(master_df['Date'])}")
print(f"Total sum: ${sum(master_df['Total Price'])}")
sorted_df = master_df.groupby('Customer Name')['Total Price'].sum()
sorted_df = DataFrame(sorted_df)
sorted_df = sorted_df.sort_values('Total Price', ascending=False)
sorted_df.to_csv("summary_report.csv")
print("Saved data to summary_report.csv.")