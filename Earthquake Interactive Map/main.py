import folium, streamlit, streamlit_folium, requests, os
from folium.plugins import MarkerCluster

streamlit.title("Earthquake Interactive Map")
earthquakes = requests.get('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson').json()['features']
carte = folium.Map()
cluster = MarkerCluster()

for earthquake in earthquakes:
    marker = folium.Marker(location=earthquake['geometry']['coordinates'][:2][::-1], popup=earthquake['properties']['title'])
    marker.add_to(cluster)

cluster.add_to(carte)

streamlit_folium.st_folium(carte)