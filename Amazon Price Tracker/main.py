import smtplib
import requests, html
from bs4 import BeautifulSoup as bs
import os

target = 100
password = 'mceugxqrdqohsdis'
url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0'}).text
soup = bs(page, 'html.parser')
print(soup.prettify())
price = float(soup.find('span', class_="a-offscreen").text.replace("$", ""))
name = soup.find("span", id="productTitle").text

if price < target:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user='iamandrewtech@gmail.com', password=password)
    msg = f"Subject: Low price for your product\n\nYour product, {name}, has a new low price of ${price}, which is lower than your target price of ${target}!\n{url}"
    connection.sendmail(from_addr="iamandrewtech@gmail.com", to_addrs="iamandrewtech@gmail.com", msg=msg.encode("utf-8"))
    connection.close()