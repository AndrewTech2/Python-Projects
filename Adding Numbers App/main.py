import streamlit as st

st.title("Add Numbers")
first = st.number_input(label='First Number', min_value=0.0)
second = st.number_input(label='Second Number', min_value=0.0)
button = st.button(label='Add')

if button:
    st.write(f"The result is: {first+second}")