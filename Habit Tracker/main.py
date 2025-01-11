import requests, datetime

date = str(datetime.date.today()).replace("-", '')
username = 'andrewtech'
token = 'asgd25sdaok34143'

# Creating an account
response = requests.post("https://pixe.la/v1/users", json={'token': token, 'username': username, 'agreeTermsOfService': 'yes', 'notMinor': 'yes'})
response.raise_for_status()

# Creating a graph
response = requests.post(f"https://pixe.la/v1/users/{username}/graphs", headers={'X-USER-TOKEN': token}, json={'id': 'coding', 'name': 'Coding Graph', 'unit': 'min', 'type': 'float', 'color': 'shibafu'})
response.raise_for_status()

# Creating a pixel
response = requests.post(f"https://pixe.la/v1/users/{username}/graphs/coding", headers={'X-USER-TOKEN': token}, json={'date': date, 'quantity': input("How many minutes have you coded today? > ")})
response.raise_for_status()
print(response.text)

# Updating a pixel
response = requests.put(f"https://pixe.la/v1/users/{username}/graphs/coding/{date}", headers={'X-USER-TOKEN': token}, json={"quantity": '30'})
print(response.text)

# # Removing a pixel
response = requests.delete(f"https://pixe.la/v1/users/{username}/graphs/coding/{date}", headers={'X-USER-TOKEN': token})
print(response.text)