import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
username = ""  # enter username
token = ""  # enter a user key
graph_id = ""  # enter users graph id
date = str(datetime.now().date()).replace("-", "")

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params), this creates the user
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs"
graph_config = {
    "id": graph_id,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"  # (red)
}

headers = {
    "X-USER-TOKEN": token  # secure way of entering api key
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers), this creates the user's graph
# print(response.text)

post_pixel = f"{PIXELA_ENDPOINT}/{username}/graphs/{graph_id}"
post_config = {
    "date": date,
    "quantity": ""  # add data of the day
}

# response = requests.post(url=post_pixel, json=post_config, headers=headers), to post data for the day in the graph
# (response.text)

update_pixel = f"{PIXELA_ENDPOINT}/{username}/graphs/{graph_id}/{date}"
update_config = {
    "quantity": ""  # changes old data to this quantity
}

# response = requests.put(url=update_pixel, json=update_config, headers=headers), to update date data in the graph
# print(response.text)

delete_pixel = f"{PIXELA_ENDPOINT}/{username}/graphs/{graph_id}/{date}"

# response = requests.delete(url=delete_pixel, headers=headers), removes data for date
# print(response.text)
