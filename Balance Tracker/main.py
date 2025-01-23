import streamlit, os, pandas, datetime
import plotly_express as plt

streamlit.title("Balance Tracker")

if 'balance_data.csv' in os.listdir():
    data = pandas.read_csv("balance_data.csv")
    balance = sum(data['Amount'])
    streamlit.header(f"Current balance: {balance}$")
    plot = plt.line(data, x='Date', y='Balance')
    streamlit.plotly_chart(plot)
    income = streamlit.number_input("Add Income (if any):", min_value=0.0)
    expenses = streamlit.number_input("Add Expenses (if any):", min_value=0.0)
    submit = streamlit.button("Submit")
    if submit and (income or expenses):
        data_dict = data.to_dict(orient="records")
        data_dict.append({'Date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'Amount': income - expenses, 'Balance': sum(data['Amount']) + (income - expenses)})
        print(data)
        data = pandas.DataFrame(data_dict)
        data.to_csv("balance_data.csv", index=False)
        streamlit.rerun()
else:
    balance = streamlit.number_input("Current balance:")
    submit = streamlit.button("Submit")
    if submit and balance:
        dta = pandas.DataFrame({'Date': [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")], 'Amount': [balance], 'Balance': [balance]})
        dta.to_csv("balance_data.csv", index=False)
        streamlit.rerun()