import json, streamlit, pandas

with open("invoice_data.json", 'rb') as file:
    data = json.load(file)

streamlit.title("Invoice")
streamlit.header(data['business_name'])
streamlit.write(data['business_address'])
streamlit.header(f"Bill to: {data['customer_name']}")
streamlit.write(data['customer_address'])
df = pandas.DataFrame(data['items'])
df['Total'] = df['Quantity'] * df['Unit Price']
subtotal = sum(df['Total'].to_list())
tax = subtotal * data['tax_rate']
total = subtotal + tax

streamlit.table(df)
streamlit.table({'Subtotal': round(subtotal, 2), 'Tax': round(tax, 2), 'Total': round(total, 2)})