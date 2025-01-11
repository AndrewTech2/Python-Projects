import folium, pandas
import folium.plugins
import streamlit, streamlit_folium

df = pandas.read_csv("accidents.csv", sep=';')
carte = folium.Map(location=(df['LATITUDE'].mean(), df['LONGITUD'].mean()))
cluster = folium.plugins.MarkerCluster()

for x in range(len(df['LATITUDE'])):
    point = folium.Marker(location=(df['LATITUDE'][x], df['LONGITUD'][x]), popup=df['MAN_COLLNAME'][x])
    point.add_to(cluster)
cluster.add_to(carte)

streamlit.title("Vehicle Accidents USA Map")
streamlit_folium.st_folium(carte)