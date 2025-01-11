from multiprocessing.managers import Value

import streamlit, pandas

streamlit.title("Employee Data Visualizer")
df = pandas.read_csv("employees.csv")
streamlit.write("Data")
streamlit.table(df)
options = []
for column in df.columns:
    try:
        temp = int(df[column][0])
        options.append(column)
    except ValueError:
        continue
selected_column = streamlit.selectbox(label='Select a column to view:', options=options)
values = df[selected_column].to_list()
names = df['Name']
streamlit.line_chart(data={selected_column: values, 'Names': names.to_list()},x='Names',y=selected_column, x_label='Names', y_label=selected_column)
