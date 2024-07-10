# this code is for ISS sightings in NYC specifically

import requests
from datetime import datetime
import smtplib
import time

NYC_LAT = 40.712776
NYC_LONG = -74.005974

MY_EMAIL = ""  # enter email to send from in the quotes
MY_PASSWORD = ""  # enter app password for email in the quotes

TO_EMAIL = ""  # enter email to send to in the quotes


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # ISS position is considered overhead within +5 or -5 degrees of NYC in this code
    if NYC_LAT - 5 <= iss_latitude <= NYC_LAT + 5 and NYC_LONG - 5 <= iss_longitude <= NYC_LONG + 5:
        return True


def is_night():
    time_now = int(datetime.now().hour)

    parameters = {
        "lat": NYC_LAT,
        "lng": NYC_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # checks if its night because its only visible at night
    if time_now > sunset or time_now < sunrise:
        return True


while True:
    # runs code every minute
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_EMAIL,
                                msg="Subject:ISS Sighting\n\nLook up into the sky in NYC to try finding the ISS!")
