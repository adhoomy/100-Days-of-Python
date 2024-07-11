# this code is to send NYC rain alert messages on WhatsApp
# number must be in twilio whatsapp server to receive messages

import requests
from twilio.rest import Client

owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = ""  # enter api key in the quotes

account_sid = ""  # enter api account sid in the quotes
auth_token = ""  # enter api auth token in the quotes

params = {
    "lat": 40.712776,
    "lon": -74.005974,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(owm_endpoint, params=params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour in range(0, 3):
    if weather_data["list"][hour]["weather"][0]["id"] < 600:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:",    # enter number to send from in the quotes
        body="Reminder: It's going to rain today, bring an umbrella! ☂️",
        to='whatsapp:'  # enter number to send to in the quotes
    )
    print(message.status)
