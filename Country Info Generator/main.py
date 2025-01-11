import requests
from urllib3 import request

country = input("What's your country? > ").capitalize()

response = requests.get(f"https://restcountries.com/v3.1/name/{country}")
try:
    response.raise_for_status()
except requests.exceptions.HTTPError:
    print("Value not found!")
    exit()
data = response.json()

languages = ", ".join(data[0]['languages'].values())

print(f"Capital: {data[0]['capital'][0]}\nRegion: {data[0]['region']}\nPopulation: {data[0]['population']}\nLanguages: {languages}")