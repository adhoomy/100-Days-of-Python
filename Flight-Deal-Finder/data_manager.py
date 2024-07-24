import os
import requests
from flight_search import FlightSearch

flight_search = FlightSearch()


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_URL = os.environ.get('FD_SHEETY_URL')
        self.SHEETY_TOKEN = os.environ.get('FD_SHEETY_TOKEN')
        self.SHEETY_HEADERS = {
            "Authorization": self.SHEETY_TOKEN
        }
        self.price_data = {}

    def get_sheet_price_data(self):
        response = requests.get(url=self.SHEETY_URL, headers=self.SHEETY_HEADERS)
        data = response.json()
        self.price_data = data['prices']
        return self.price_data

    def update_location_code(self):
        for city in self.price_data:
            name = city['city']
            city_code = flight_search.get_city_code(city_name=name)
            # new_data must have a root named price because the original json file from sheety has the root named price
            new_data = {
                'price': {
                    'iataCode': city_code
                }
            }
            requests.put(url=f"{self.SHEETY_URL}/{city['id']}", json=new_data, headers=self.SHEETY_HEADERS)
        return self.price_data
