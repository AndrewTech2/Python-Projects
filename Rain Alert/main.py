import requests, smtplib

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params={'lat': 48.111778, 'lon': -1.680260, 'appid': "212e4c7f0af9fe95216520bf4e94a8f8", 'cnt': 4, 'units': 'metric'})
response.raise_for_status()
data = response.json()
weather_codes = []
hours_raining = []
raining = False

for day in data['list']:
    weather_id = day['weather'][0]['id']
    weather = day['weather'][0]['main'] + " | " + day['weather'][0]['description']
    hour = "".join(day['dt_txt'].split()[1])
    weather_codes.append({'id': weather_id, 'weather': weather, 'hours': hour})
    if weather_id < 700:
        hours_raining.append(hour)
        raining = True

if raining:
    if len(hours_raining) != 1:
        hours = ", ".join(hours_raining)
    else:
        hours = hours_raining[0]
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user='iamandrewtech@gmail.com', password="uilujznskxzsffyi")
    connection.sendmail(from_addr='iamandrewtech@gmail.com', to_addrs="iamandrewtech@gmail.com", msg=f"Subject: Take an umbrella!\n\nHi there! It's going to rain today at {hours}, so take an umbrella!")
    connection.close()