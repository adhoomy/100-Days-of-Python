import os
import requests
from pprint import pprint

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.FLIGHT_SEARCH_KEY = os.environ.get('AMADEUS_KEY')
        self.FLIGHT_SEARCH_SECRET = os.environ.get('AMADEUS_SECRET')
        self.flight_search_token = self.get_new_token()

    def get_city_code(self, city_name):
        params = {
            'keyword': city_name
        }
        # response = requests.get(url=IATA_ENDPOINT, params=params)
        code = "iataCode"
        return code

    def get_new_token(self):
        # Header with content type as per Amadeus documentation
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.FLIGHT_SEARCH_KEY,
            'client_secret': self.FLIGHT_SEARCH_SECRET
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        print(response.text)
        return response
