import streamlit as st

st.title("BMI Calculator")
height = st.number_input("Enter your height in centimeters:", min_value=40, step=1, max_value=250)
weight = st.number_input("Enter your weight in kilograms:", min_value=20.0, step=0.5, max_value=250.0)
button = st.button("Calculate")
if button:
    st.write(f"Your BMI: {round(weight / ((height/100)**2), 2)}")