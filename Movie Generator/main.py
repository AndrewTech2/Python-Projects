from bs4 import BeautifulSoup as bs
import requests

content = requests.get("https://www.empireonline.com/movies/features/best-movies-2/").text
soup = bs(content, 'html.parser')
titles = []

for title in soup.find_all("h3", {'class': "listicleItem_listicle-item__title__BfenH"})[::-1]:
    titles.append(title.text)

with open("top_100_films.txt", 'w') as file:
    for title in titles:
        file.write(f"{title}\n")