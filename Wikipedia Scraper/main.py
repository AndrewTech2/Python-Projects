import requests
from bs4 import BeautifulSoup as bs

content = requests.get("https://en.wikipedia.org/wiki/Mathematics").text
soup = bs(content, 'html.parser')
paragraphs = soup.find_all("p")
with open("article.txt", 'w') as file:
    for para in paragraphs[:5]:
        file.write(para.text)
        file.write("\n")