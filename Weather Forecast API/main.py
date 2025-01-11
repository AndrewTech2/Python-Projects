from flask import Flask
import random

weather_conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Snowy"]
app = Flask(__name__)

@app.route("/forecast/<city>")
def forecast(city):
    forecasts = []
    for day in range(1, 4):
        forecasts.append({'day': f'Day {day}', 'temperature_c': random.randint(-40, 40), 'condition': random.choice(weather_conditions)})
    return {'city': city.title(), 'forecasts': forecasts}

@app.route("/forecast/<city>/<day_id>")
def forecast_day(city, day_id):
    try:
        if not int(day_id) in range(1, 4):
            return {'error': 'Sorry, our free API provides a 3-day weather forecast.', 'status': 400}
    except ValueError:
        return {'error': 'Invalid day ID.', 'status': 400}
    return {'city': city.title(), 'forecast': {'day': f'Day {day_id}', 'temperature_c': random.randint(-40, 40), 'condition': random.choice(weather_conditions)}}

app.run(debug=True)