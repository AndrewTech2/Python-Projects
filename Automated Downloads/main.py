import requests

with open("stations.txt", 'r') as file:
    stations = file.read().split("\n")

for station in stations:
    data = requests.get(f"https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_station/{station}.csv.gz").content
    with open(f"{station}.txt", 'wb') as file:
        file.write(data)