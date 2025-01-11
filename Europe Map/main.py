import streamlit, pandas, folium, streamlit_folium

streamlit.title("Europe Map")
df = pandas.read_csv("europe.csv")
carte = folium.Map()
countries = {}
for ind in range(52):
    countries[df['Country'][ind]] = {'Latitude': df['Latitude'][ind], 'Longitude': df['Longitude'][ind]}
for country in countries:
    marker = folium.CircleMarker(location=(countries[country]['Latitude'], countries[country]['Longitude']), popup=folium.Popup(country), fill=True)
    marker.add_to(carte)

streamlit_folium.st_folium(carte)