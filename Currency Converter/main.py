import requests, datetime

api_key = "d2fcab9607cc2a41403e5f57"
base = input("Base Currency > ").upper()
target = input('Target Currency > ').upper()
amount = float(input(f'Amount in {base} > '))

data = requests.get(f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base}").json()
if data['result'] == 'error':
    if data['error-type'] == 'unsupported-code':
        print("Unsupported currency.")
        exit()
rates = data['conversion_rates']
if target not in rates.keys():
    print("Target currency not found / not supported.")
else:
    print(f"Result: {amount} {base} = {amount*rates[target]} {target}")
    with open("currency_conversion.txt", 'w') as file:
        file.write(f"Base Currency: {base}\nAmount: {amount} {base}\n{amount} {base} = {amount*rates[target]} {target}\nTimestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Results saved!")