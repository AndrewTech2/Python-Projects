from bs4 import BeautifulSoup as bs
import requests

lat = float(input("Latitude > "))
lon = float(input("Longitude > "))
content = requests.get(f"https://weather.com/weather/today/l/{lat},{lon}").text
soup = bs(content, 'html.parser')
temp = soup.find("span", {'class': 'CurrentConditions--tempValue--zUBSz'}).text
print(f"Current temperature: {temp}")