import requests, pandas

content = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson").json()
earthquakes_list = [{'Name': earthquake['properties']['title'], 'Location': earthquake['properties']['place'], 'Magnitude': earthquake['properties']['mag'], 'URL': earthquake['properties']['url']} for earthquake in content['features']]
earthquakes = pandas.DataFrame(earthquakes_list)
earthquakes = earthquakes.sort_values('Magnitude', ascending=False)
print("Top 10 Earthquakes in the past week:")
print(earthquakes[:10])
earthquakes.to_csv("earthquakes.csv")