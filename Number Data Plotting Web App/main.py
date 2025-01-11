import streamlit as st

st.title("Number Data Visualization")
st.line_chart(data={'Letters': ['a', 'b', 'c', 'd'], 'Percentages': [1123,253420, 12541230,115440]}, x='Letters', y='Percentages')