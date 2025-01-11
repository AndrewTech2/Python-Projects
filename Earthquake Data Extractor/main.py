import datetime, requests, pandas as pd

today = datetime.date.today()
yesterday = datetime.date(year=today.year, month=today.month, day=today.day-1)
response = requests.get("https://earthquake.usgs.gov/fdsnws/event/1/query", params={'format': 'geojson', 'starttime': str(yesterday)})
data = response.json()
earthquakes = [{'Magnitude': earthquake['properties']['mag'], 'Location': earthquake['properties']['place'], 'Latitude': earthquake['geometry']['coordinates'][0], 'Longitude': earthquake['geometry']['coordinates'][1]} for earthquake in data['features']]
df = pd.DataFrame(earthquakes)
df.to_csv(index=False, path_or_buf=f'earthquake-data-{yesterday}')