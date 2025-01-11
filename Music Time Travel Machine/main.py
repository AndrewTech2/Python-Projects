from bs4 import BeautifulSoup as bs
import requests, datetime, spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = "eb3d1a0df5a4442e918ff3aaf10833e7"
client_secret = "2c081876a3e3407d904b0a38c2e82097"

date = input("Date to which you want to travel back to (YYYY-MM-DD) > ")
try:
    year = int(date.split("-")[0])
    month = int(date.split("-")[1])
    day = int(date.split("-")[2])
    dt = datetime.date(year=year, month=month, day=day)
    if year < 2000:
        raise ValueError
    if datetime.date.today() <= dt:
        raise ValueError
except:
    print("Invalid date.")
    exit()

page = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}).text
soup = bs(page, 'html.parser')
titles = soup.select('div ul li h3')
titles_list = []
for title in titles:
    title = title.text
    title = title.replace("\t", "")
    title = title.replace("\n", "")
    titles_list.append(title)


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, scope='playlist-modify-private', redirect_uri="https://www.example.com"))
id = sp.current_user()['id']
urls = []
for title in titles_list:
    try:
        track = sp.search(q=title, limit=1)['tracks']['items'][0]['external_urls']['spotify']
        urls.append(track)
    except:
        continue
try:
    det = sp.user_playlist_create(user=id, name=f"{date} Top 100", public=False)
except:
    print("Playlist already exists!")
    exit()
play_id = det['id']
for url in urls:
    sp.playlist_add_items(playlist_id=play_id, items=[url])