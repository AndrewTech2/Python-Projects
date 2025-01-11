import requests
from datetime import datetime
import smtplib
import time

while True:
    MY_LAT = 51.507351 # Your latitude
    MY_LONG = -0.127758 # Your longitude
    user = "iamandrewtech@gmail.com"
    password = 'vtwjcfmjtecakfya'

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    def is_close():
        if abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <= 5:
            return True
        return False

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour = time_now.hour

    #If the ISS is close to my current position
    # ,and it is currently dark
    # Then email me to tell me to look up.
    # BONUS: run the code every 60 seconds.
    if is_close():
        if sunrise > hour or sunset < hour:
            print("Found")
            connection = smtplib.SMTP('smtp.gmail.com')
            connection.starttls()
            connection.login(user=user, password=password)
            connection.sendmail(from_addr=user, to_addrs=user, msg=f"Subject: Look up!\n\nThe ISS (International Space Station) is currently flying over you and it might be visible! It's exact coordinates are {iss_latitude} (latitude), {iss_longitude} (longitude).")
            connection.close()
        else:
            pass
    time.sleep(60)
