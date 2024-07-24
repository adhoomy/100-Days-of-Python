#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from pprint import pprint
import data_manager

data_manager = data_manager.DataManager()

sheet_data = data_manager.get_sheet_price_data()
# pprint(sheet_data)

new_data = data_manager.update_location_code()
# pprint(new_data)
