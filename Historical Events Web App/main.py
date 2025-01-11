import streamlit as st
import requests

st.title("Historical Events Generator")
st.write("Enter a date and see all events that happened on that day.")
month = st.number_input("Enter the month (1 for January):", min_value=1, step=1, max_value=12)
day = st.number_input("Enter the day:", min_value=1, max_value=31, step=1)
button = st.button("Search events")

if button:
    try:
        events = requests.get(f"http://history.muffinlabs.com/date/{month}/{day}").json()
    except:
        st.write("No events found for that date. Are you sure it exists? 30th and 31st of February do not.")
    else:
        for event in events['data']['Events']:
            st.write(f"Year: {event['year']}")
            st.write(f"Description: {event['text']}")
            st.write(f"Link: {event['links'][0]['link']}")