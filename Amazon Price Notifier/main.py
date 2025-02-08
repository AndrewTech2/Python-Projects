from bs4 import BeautifulSoup
import requests, time, os

def get_price():
    """Gets the price of the product."""
    page = requests.get("https://www.amazon.com/PF-WaterWorks-PF0989-Disposal-Installation/dp/B078H38Q1M/").text
    soup = BeautifulSoup(page, 'html.parser')
    new = float(f"{soup.find('span', {'class': "a-price-whole"}).text}{soup.find("span", {'class': 'a-price-fraction'}).text}")
    return new

if 'last_price.txt' in os.listdir():
    with open("last_price.txt", 'r') as file:
        price = float(file.read())
else:
    price = get_price()

while True:
    new_price = get_price()
    if new_price != price:
        mes = requests.post("https://ntfy.sh/amazon_price_notifier", data=f'New price detected! The old price was {price}$, and the new one is {new_price}$!')
        price = new_price
        with open("last_price.txt", 'w') as file:
            file.write(f"{price}")
    time.sleep(10)