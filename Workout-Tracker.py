import requests
from datetime import datetime

APP_ID = ""  # enter app id in the quotes
API_KEY = ""  # enter api key in the quotes
NLE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NLE_HEADER = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
WEIGHT = 0  # set weight in kg
HEIGHT = 0  # set height in cm
AGE = 1  # set age (must be at least 1)
SHEETY_ENDPOINT = ""  # enter sheety project url in the quotes
SHEETY_USERNAME = ""  # enter username for sheety project in the quotes
SHEETY_AUTHORIZATION = ""  # enter authorization for sheety project in the quotes
SHEETY_HEADERS = {
    "Authorization": SHEETY_AUTHORIZATION
}

exercises = input("Tell me what exercises you did: ")

nle_params = {
    "query": exercises,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=NLE_ENDPOINT, headers=NLE_HEADER, json=nle_params)
exercise_data = response.json()

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")

sheets_params = {
    "workout": {
        "Content-Type": "application/json",
        "date": date,
        "time": time,
        "exercise": exercise_data["exercises"][0]["name"].title(),
        "duration": exercise_data["exercises"][0]["duration_min"],
        "calories": exercise_data["exercises"][0]["nf_calories"]
    }
}

post_row = requests.post(url=SHEETY_ENDPOINT, json=sheets_params, headers=SHEETY_HEADERS)
