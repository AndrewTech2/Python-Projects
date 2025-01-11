import streamlit as st
from streamlit import form_submit_button

st.title("Distance Converter: Miles - Kilometres")
option = st.selectbox('Choose method', options=['mi to km', 'km to mi'])

if option == 'Mi to KM':
    miles = st.number_input("Enter the distance in miles:", min_value=0.0)
    if miles != 0:
        st.success(f"{miles} miles are equal to {round(miles * 1.61, 2)} kilometres.")
else:
    km = st.number_input("Enter the amount in kilometres:", min_value=0.0)
    if km != 0:
        st.success(f"{km} kilometres are equal to {round(km * 0.62, 2)} miles.")