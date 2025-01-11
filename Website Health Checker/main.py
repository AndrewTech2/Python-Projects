import requests, pandas, datetime

websites = []
with open("websites.txt", 'r') as file:
    for line in file.readlines():
        websites.append(line.replace("\n", ''))
print(f"Checking {len(websites)} websites...")
response_time_column = []
status_code = []
status = []
for website in websites:
    initial = datetime.datetime.now()
    try:
        response = requests.get(website)
        time_after_response = datetime.datetime.now()
        response_time = time_after_response - initial
        response_time_column.append(response_time.microseconds)
    except requests.exceptions.ConnectionError:
        print(f"{website} - Offline - N/A")
        response_time_column.append('N/A')
        status_code.append("N/A")
        status.append('Offline')
        continue
    if response.status_code == 200:
        print(f"{website} - Online - 200")
        status.append("Online")
    else:
        print(f"{website} - Offline - {response.status_code}")
        status.append('Offline')
    status_code.append(response.status_code)
    print('Response Time:', response_time.microseconds)
log = pandas.DataFrame({'URL': websites, 'Response Time (ms)': response_time_column, 'Status Code': status_code, 'Status': status})
log.to_csv("log.csv")