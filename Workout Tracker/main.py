import requests, datetime, os

today = str(datetime.date.today()).replace("-", "/")
now = datetime.datetime.now()
time = str(now.time())[:5] + ":00"

app_id = "89246865"
api_key = 'c4cbd6546255d516fa53c808764c3877'
auth = "Basic YW5kcmV3dGVjaDpmZGFzdTM0MTNidmVkODQ1"

response = requests.post('https://trackapi.nutritionix.com/v2/natural/exercise', headers={'x-app-id': app_id, 'x-app-key': api_key}, json={'query': input("What exercise did you do today? > ")})
data = response.json()
calories = int(data['exercises'][0]['nf_calories'])
name = data['exercises'][0]['name'].title()
duration = int(data['exercises'][0]['duration_min'])

response = requests.post("https://api.sheety.co/3a29184ad8ddb9d144e36f98ad2ebac4/myWorkouts/workouts", json={'workout': {'date': today, 'time': time, 'exercise': name, 'duration': duration, 'calories': calories}}, headers={'Authorization': auth})