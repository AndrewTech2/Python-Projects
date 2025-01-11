from datetime import timedelta

import requests, smtplib, datetime

today = datetime.date.today() + timedelta(days=1)
end = str(today + datetime.timedelta(days=150))
today = str(today)
api_secret = "39rTXs2b3ulyVMYj"
api_key = "6xzXYJSwUm4lZ39l7nuh0NZvoOe2DYiD"
access_token = 'xbwSZr4zui2GBEZBcUhyAN6LAebN'

# Adding the IATA codes
# response = requests.get("https://api.sheety.co/3a29184ad8ddb9d144e36f98ad2ebac4/flightDeals/prices", headers={"Authorization": "Basic YW5kcmV3OmZldzM0ODFqZjM4MjM1cjQy"})
# cities_dict = response.json()
# cities = []
# for city in cities_dict['prices']:
#     cities.append(city['city'])
#
# for city in cities:
#     response = requests.get("https://test.api.amadeus.com/v1/reference-data/locations/cities", headers={'Authorization': f"Bearer {access_token}"}, params={"keyword": city})
#     response.raise_for_status()
#     iata_data = response.json()
#     iata = iata_data['data'][0]['iataCode']
#     ind = cities.index(city)
#
#     response = requests.put(f"https://api.sheety.co/3a29184ad8ddb9d144e36f98ad2ebac4/flightDeals/prices/{ind+2}", headers={'Authorization': "Basic YW5kcmV3OmZldzM0ODFqZjM4MjM1cjQy"}, json={'price': {"iataCode": iata}})
#     response.raise_for_status()
#     print(response.text)

# Creating an access token
# response = requests.post("https://test.api.amadeus.com/v1/security/oauth2/token", headers={'Content-Type': "application/x-www-form-urlencoded"}, data={'grant_type': "client_credentials", 'client_id': api_key, 'client_secret': api_secret})
# print(response.text)

response = requests.get("https://api.sheety.co/3a29184ad8ddb9d144e36f98ad2ebac4/flightDeals/prices", headers={"Authorization": "Basic YW5kcmV3OmZldzM0ODFqZjM4MjM1cjQy"})

cities = response.json()['prices']
iata_dict = {}
for x in cities:
    iata_dict[x['iataCode']] = {'city': x['city'], 'lowestPrice': x['lowestPrice']}

for iata in iata_dict:
    response = requests.get("https://test.api.amadeus.com/v1/shopping/flight-dates", headers={'Authorization': f'Bearer {access_token}'}, params={'origin': 'LON', 'destination': iata, 'nonStop': 'true', 'oneWay': 'true', 'departureDate': f"{today},{end}"})
    data = response.json()
    print(data)
    if 'errors' in data.keys():
        if data['errors'][0]['code'] == 6003:
            response = requests.get("https://test.api.amadeus.com/v1/shopping/flight-dates", headers={'Authorization': f'Bearer {access_token}'}, params={'origin': 'LON', 'destination': iata, 'nonStop': 'false', 'oneWay': 'true', 'departureDate': f"{today},{end}"})
            data = response.json()
            if 'errors' in data.keys():
                continue
        else:
            continue
    price = float(data['data'][0]['price']['total'])
    if price < iata_dict[iata]['lowestPrice']:
        date = data['data'][0]['departureDate']

        response = requests.get("https://api.sheety.co/3a29184ad8ddb9d144e36f98ad2ebac4/flightDeals/users", headers={"Authorization": "Basic YW5kcmV3OmZldzM0ODFqZjM4MjM1cjQy"})
        emails_dict = response.json()
        emails = []
        print(emails_dict)
        for x in emails_dict['users']:
            emails.append(x['email'])

        for email in emails:
            try:
                connection = smtplib.SMTP("smtp.gmail.com")
                connection.starttls()
                connection.login(user="iamandrewtech@gmail.com", password="dlcwhdbombwqhcos")
                connection.sendmail(from_addr='iamandrewtech@gmail.com', to_addrs=email, msg=f"Subject: Cheap Deal Found!\n\nLow Price Alert! Only {price} euros to fly from London to {iata_dict[iata]['city']}, on {date}.")
                connection.close()
            except:
                continue