import streamlit, requests

api_key = '212e4c7f0af9fe95216520bf4e94a8f8'
streamlit.title("Weather Dashboard")
city = streamlit.text_input(label="Target city: ", placeholder='Add a city...')
button = streamlit.button(label='Get Weather')
if button and city.title():
    weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric").json()
    if weather['cod'] != 200:
        streamlit.subheader("I'm sorry, an unexpected error has occured. Check if the city's name is correct.")
    else:
        streamlit.header(weather['name'])
        streamlit.image(f"https://openweathermap.org/img/wn/{weather['weather'][0]['icon']}@2x.png")
        streamlit.subheader(f"Temperature: {weather['main']['temp']}°C")
        streamlit.subheader(f"Humidity: {weather['main']['humidity']}%")
        streamlit.subheader(f'Weather: {weather['weather'][0]['description']}')
        streamlit.subheader(f"Wind Speed: {weather['wind']['speed']} m/s")