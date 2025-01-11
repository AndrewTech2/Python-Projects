from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
import requests, time

form = 'https://forms.gle/aKvfThBAH6oecZ5G9'

webpage = requests.get("https://appbrewery.github.io/Zillow-Clone/").text
soup = bs(webpage, 'html.parser')
prices = []
links = []
addresses = []

for price in soup.find_all("span", {'class': 'PropertyCardWrapper__StyledPriceLine'}):
    prices.append(price.text.replace("/mo", '').replace('+', '').replace('1 bd', '').replace("1bd",''))
for link in soup.find_all('a', {'class': 'property-card-link'}):
    href = link['href']
    links.append(href)
for address in soup.find_all('address', {'data-test': 'property-card-addr'}):
    addresses.append(address.text.replace('\n', '').replace('  ', ''))

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)
driver.maximize_window()

for x in range(len(prices)):
    driver.get(form)
    time.sleep(1.5)

    addr = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    addr.send_keys(addresses[x])

    prc = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    prc.send_keys(prices[x])

    lnk = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    lnk.send_keys(links[x])

    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()
