import requests, smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
key = "WB8SQCA2IJJ9Z59D"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response = requests.get("https://www.alphavantage.co/query", params={'function': 'TIME_SERIES_DAILY', 'symbol': STOCK, 'apikey': key})
response.raise_for_status()
stock_data = response.json()
today = float(stock_data['Time Series (Daily)'][list(stock_data['Time Series (Daily)'].keys())[0]]['4. close'])
yesterday = float(stock_data['Time Series (Daily)'][list(stock_data['Time Series (Daily)'].keys())[7]]['4. close'])
difference = today - yesterday
perc = round(abs(difference) / yesterday * 100, 1)
if perc >= 0:

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    response = requests.get("https://www.newsapi.org/v2/top-headlines", params={'apiKey': '1931da56f34a469d825e16a5e4328283', 'q': COMPANY_NAME})
    response.raise_for_status()
    news_data = response.json()
    source = news_data['articles'][0]['source']['name']
    title = news_data['articles'][0]['title']
    desc = news_data['articles'][0]['description']
    url = news_data['articles'][0]['url']

    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(user="iamandrewtech@gmail.com", password="ojoteggipzzmrpsu")
    connection.sendmail(from_addr="iamandrewtech@gmail.com", to_addrs="iamandrewtech@gmail.com", msg=f"Subject: Stock Market Change\n\n{STOCK}: {"-" if difference < 0 else "⬆"} {perc}%\n\nLatest Article:\n\nSource: {source} - {url}\n{title}\n{desc}")
    connection.close()
