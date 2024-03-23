import requests
from datetime import datetime

USERNAME = "sharma217"
TOKEN = "hwnd7w09wud82s3Du2"
GRAPH_ID = "graph12"
pixela_endpoint = "https://pixe.la/v1/users"

# Create user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Create graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "my cycling graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Add pixel data
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# Corrected the way today is initialized
today = datetime(year=2024, month=3, day=21)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "21.74"
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
